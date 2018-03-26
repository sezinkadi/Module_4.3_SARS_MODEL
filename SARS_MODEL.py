import matplotlib.pyplot as plt
t=0
simLength=200
dt=0.25

susceptible = 999999
infectuous_undetected = 0
exposed = 1
N0 = susceptible+exposed
k = 10
b = 0.06
q = 0
sus_to_expos = k * b * (1 - q) * infectuous_undetected * susceptible / N0
p = 0.2
expos_to_undet = p * exposed
sus_to_expos_quar = q * k* b * infectuous_undetected * susceptible / N0
exposed_quarantined = 0
expos_quar_to_inf_quar = p * exposed_quarantined
w = 0.0375
undet_to_iso = w * infectuous_undetected
infectuous_quarantined = 0
inf_quar_to_iso = w * infectuous_quarantined
infectuous_isolated = 0
v = 0.0625
iso_to_immune = v * infectuous_isolated
m = 0.1
iso_to_death = m * infectuous_isolated
quar_to_death = m * infectuous_quarantined
inf_quar_to_rec = v * infectuous_quarantined
undet_to_death = m * infectuous_undetected
undet_to_im = v * infectuous_undetected
susceptible_quarantined = 0
sus_to_quar = q * k * (1 - b) * infectuous_undetected * susceptible / N0
u = 0.1
quar_to_sus = u * susceptible_quarantined
recovered_immune = 0
SARS_death = 0
infecteds_total = exposed + exposed_quarantined + infectuous_undetected + infectuous_quarantined + infectuous_isolated
R = k * b * (1 - q) /(v + m + w)


timeLst=[t]
infectedLst=[infecteds_total]
recoveredLst=[recovered_immune]
deathLst=[SARS_death]
while t<200:
 t=t+dt
 susceptible = susceptible + (quar_to_sus - sus_to_expos - sus_to_expos_quar - sus_to_quar) * dt
 infectuous_undetected = infectuous_undetected + (expos_to_undet - undet_to_iso - undet_to_death - undet_to_im) * dt
 exposed = exposed + (sus_to_expos - expos_to_undet) * dt
 exposed_quarantined = exposed_quarantined + (sus_to_expos_quar - expos_quar_to_inf_quar) * dt
 infectuous_quarantined = infectuous_quarantined+ (expos_quar_to_inf_quar - quar_to_death - inf_quar_to_iso - inf_quar_to_rec) * dt
 infectuous_isolated = infectuous_isolated + (undet_to_iso + inf_quar_to_iso - iso_to_immune - iso_to_death) * dt
 susceptible_quarantined= susceptible_quarantined + (sus_to_quar - quar_to_sus) * dt
 recovered_immune = recovered_immune + (iso_to_immune + undet_to_im + inf_quar_to_rec) * dt
 SARS_death = SARS_death + (quar_to_death + iso_to_death + undet_to_death) * dt
 N0 = susceptible + exposed
 sus_to_expos = k * b * (1 - q) * infectuous_undetected * susceptible / N0
 expos_to_undet = p * exposed
 sus_to_expos_quar = q * k* b * infectuous_undetected * susceptible / N0
 expos_quar_to_inf_quar = p * exposed_quarantined
 undet_to_iso = w * infectuous_undetected
 inf_quar_to_iso = w * infectuous_quarantined
 iso_to_immune = v * infectuous_isolated
 iso_to_death = m * infectuous_isolated
 quar_to_death = m * infectuous_quarantined
 inf_quar_to_rec = v * infectuous_quarantined
 undet_to_death = m * infectuous_undetected
 undet_to_im = v * infectuous_undetected
 sus_to_quar = q * k * (1 - b) * infectuous_undetected * susceptible / N0
 quar_to_sus = u * susceptible_quarantined
 infecteds_total = exposed + exposed_quarantined + infectuous_undetected + infectuous_quarantined + infectuous_isolated
 R = k * b * (1 - q) /(v + m + w)
 timeLst.append(t)
 infectedLst.append(infecteds_total)
 recoveredLst.append(recovered_immune)
 deathLst.append(SARS_death)
plt.plot(timeLst,infectedLst, color='g')
plt.text(150,58000,'Infecteds',color='g')
plt.plot(timeLst,recoveredLst,color='b')
plt.text(150,300000,'Recovereds',color='b')
plt.plot(timeLst,deathLst,color='r')
plt.text(150,500000,'Deaths',color='r')
plt.show()
