## Slam_orb3

Este trabajo fue implementado en base a ORB_SLAM3, se puede acceder en el siguiente enlace: https://github.com/UZ-SLAMLab/ORB_SLAM3.

### Resultados
El resultado obtenido se muestra en la siguiente animacion.

![Alt Text]('https://github.com/antbenar/Slam_orb3/blob/master/Assets/resultados.gif')


### Ejecucion

Se implementaron los scripts necesarios para correr Slam. En la carpeta Scripts. 
Para generar el formato de entrada para ORB_SLAM3 desde un video .mp4 usar el siguiente comando:

```bash
scripts/launch_video2img.sh
```

Luego copiar la primera columna del resultado en 'Datasets/TEST_1/mav0/cam0/data.csv' a 'Datasets/TEST_1/mav0/timestamp.txt'.

Para ejecutar ORB_SLAM3 con la data previamente preparada, ejecutar el siguiente comando:

```bash
./run_ORB_SAM3.sh
```

Use este codigo con sabiduria.
