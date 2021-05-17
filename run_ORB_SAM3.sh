#!/bin/bash
pathDatasetEuroc="$PWD/Datasets" #Example, it is necesary to change it by the dataset path

#------------------------------------
# Monocular Examples
echo "Launching MH01 with Monocular sensor"

#./Monocular/mono_euroc ../Vocabulary/ORBvoc.txt ./Monocular/EuRoC.yaml "$pathDatasetEuroc/TEST_3" ./Datasets/TEST_3/mav0/timestamp.txt dataset-test_3_robotica

#./Monocular/mono_euroc ../Vocabulary/ORBvoc.txt ./Monocular/EuRoC.yaml "$pathDatasetEuroc/TEST_2" ./Datasets/TEST_2/mav0/timestamp.txt dataset-test_2_robotica

./Monocular/mono_euroc ../Vocabulary/ORBvoc.txt ./Monocular/EuRoC.yaml "$pathDatasetEuroc/TEST_1" ./Datasets/TEST_1/mav0/timestamp.txt dataset-test_1_robotica