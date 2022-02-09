'''
Birinho trabalha numa empresa que fornece monitoramento para os servidores de seus clientes, sua função 
é monitorar tais servidores, como espaço em disco, memória, cpu, etc.

O sistema da empresa trabalha com threshold(limite), onde, por exemplo, quando um HD de 100 Gb 
atinge uma marca de 70% utilizado (30% livre) gera-se um alarme de "Warning", e quando o disco 
atinge 90% de utilização (10% livre) gera-se um alarme de "Critical". Porém Birinho acabou 
desconfigurando o threshold do sistema, e sua função agora é ajudá-lo a   reconfigurar esse threshold 
para a empresa continuar suas atividades.


'''

while True:
    try:
        dados = [int(x) for x in input().split()]
        total_disco = dados[0]
        armazenamento_utilizado = dados[1]
        percent_warning = dados[2]
        percent_critical = dados[3]
        x = 100 * armazenamento_utilizado / total_disco

        if x < percent_warning:
            print('OK')
        elif x < percent_critical:
            print('warning')
        else:
            print('critical')

    except EOFError:
        break