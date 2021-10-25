#include <avr/io.h>
#include <avr/interrupt.h>  /* for sei() */
#include <util/delay.h>     /* for _delay_ms() */
#include <avr/pgmspace.h>   /* required by usbdrv.h */

#include "peri.h"
#include "usbdrv.h"

#define RQ_SET_BUZZ        2
#define RQ_GET_LIGHT34     3
#define RQ_GET_INFA0       0
#define RQ_GET_INFA1       1
/* ------------------------------------------------------------------------- */
/* ----------------------------- USB interface ----------------------------- */
/* ------------------------------------------------------------------------- */
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
    usbRequest_t *rq = (void *)data;

    /* declared as static so they stay valid when usbFunctionSetup returns */
    static uint8_t infa_state1,infa_state0;
    static uint16_t light34[2] ;
    if (rq->bRequest == RQ_SET_BUZZ)
    {
        uint8_t buz_state = rq->wValue.bytes[0];
        uint8_t buz_no  = rq->wIndex.bytes[0];
        set_buz(buz_no, buz_state);
        return 0;
    }

    else if (rq->bRequest == RQ_GET_INFA0)
    {
        infa_state0 = Infa_see0();
        usbMsgPtr = &infa_state0;
        return 1;
    }
    else if (rq->bRequest == RQ_GET_INFA1)
    {
        infa_state1 = Infa_see1();
        usbMsgPtr = &infa_state1;
        return 1;
    }

    else if (rq->bRequest == RQ_GET_LIGHT34)
    {
        light34[0] = read_adc(PC3);
        light34[1] = read_adc(PC4);
        usbMsgPtr = (uchar*) &light34;
        return sizeof(light34);
    }

    return 0;

}

/* ------------------------------------------------------------------------- */
int main(void)
{
    init_peri();

    usbInit();

    /* enforce re-enumeration, do this while interrupts are disabled! */
    usbDeviceDisconnect();
    _delay_ms(300);
    usbDeviceConnect();

    /* enable global interrupts */
    sei();

    /* main event loop */
    for(;;)
    {
        usbPoll();
    }

    return 0;
}

/* ------------------------------------------------------------------------- */
