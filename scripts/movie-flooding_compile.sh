# Compile a movie (MP4) from a set of frames (PNG).

FRAMESDIR="/home/faruk/gdrive/temp_flooding_brains/frames/movie-okapi_black_shot-1"
FRAMESID="frame"

OUTPUTDIR="/home/faruk/gdrive/temp_flooding_brains/test"
OUTPUTID="okapi_test"

# -----------------------------------------------------------------------------
# Compile shots using ffmpeg
command="ffmpeg -y "
command+="-i ${FRAMESDIR}/${FRAMESID}-%03d.png "
command+="-vb 20M -c:v libx264 -vf fps=24 -pix_fmt yuv420p "
command+="${OUTPUTDIR}/${OUTPUTID}.mp4"
echo command
${command}

echo "Finished."
