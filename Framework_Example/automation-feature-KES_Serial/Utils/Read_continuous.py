from InitializeSerialDevice import SerialInit
import time

# init with 0 time out todo check if 0 time out is needed
# timeout = 0: non-blocking mode, return immediately in any case, returning zero or more, up to the requested number of bytes
sr = SerialInit(TimeOut=0)

# browse to the directory with the image recog app
sr.writePattern('cd /media')

pattern_to_write = './ImageRecognitionApplication --imageDir /media/pod_images/Dec22 --masterRecipe /sandstone_active/recipes/master_recipes.json --brandInfo /sandstone_active/recipes/master_brand_info.json | grep -e PodPresent -e Processing'
# kick off image recognition command
sr.writePattern(str(pattern_to_write))
# time.sleep(0.1)
# read until you encounter a $, means all the images were processed
sr.read_continuous('$')

# close connection
sr.closeConnection()

# if this works modify the test_Imagerecognition to use read_continuous method and expect a list <not a string>