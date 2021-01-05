seg_str = input("Por favor, Entre com o número de segundos que deseja converter em Dias, Horas, Minutos e Segundos:")
tt_segs = int(seg_str)

dias = tt_segs // 86400
tt_segs = tt_segs % 86400
horas = tt_segs // 3600
tt_segs = tt_segs % 3600
min = tt_segs // 60
tt_segs = tt_segs % 60

print(dias,"dias,",horas,"horas,",min,"minutos e",tt_segs,"segundos.")