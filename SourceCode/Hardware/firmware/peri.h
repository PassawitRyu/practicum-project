#define Infa_see0() ((PINC & (1<<PC0)) == 0)
#define Infa_see1() ((PINC & (1<<PC1)) == 0)

void init_peri();
void set_buz(uint8_t pin, uint8_t state);
uint16_t read_adc(uint8_t channel);
