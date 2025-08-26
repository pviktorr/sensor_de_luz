from machine import Pin, ADC
import time 
#config dos pinos 
#Pino para o sensor fotoresistor LDR # O pinto GPI04 sera usado para leitura analogica
PINO_LDR = 4 
# Pino do LED indicador de ambiente escuro
#O pino GPIO23
PINO_LED_ESCURO = 23
# Crie os objetos ADC e Pin com a config correta
# A Classe ADC é para leitura analogica
sensor_ldr = ADC(Pin(PINO_LDR))
# A classe Pin é para controle digital (liga/desliga o LED)
led_escuro = Pin(PINO_LED_ESCURO, Pin.OUT)
# configure a resolução do ADC para maior precisão (12bits)
sensor_ldr.width(ADC.WIDTH_12BIT)

sensor_ldr.atten(ADC.ATTN_11DB)

while True: 

  valor_luminosidade = sensor_ldr.read()

  print( "Valor de Luminosidade", valor_luminosidade)

  LIMIAR_ESCURO = 400

  if valor_luminosidade < LIMIAR_ESCURO:

    print("Ambiente escuro! Acendendo o LED.")
    led_escuro.value(1)
  else:
      print("Ambeiente Claro. LED apagado")
      led_escuro.value(0)
  time.sleep(1)