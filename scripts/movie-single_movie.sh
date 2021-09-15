# Compile a movie (MP4) from a set of frames (PNG).

FRAMESDIR="/home/faruk/gdrive/temp_flooding_brains/frames/movie-giraffe_plasma_shot-3"
FRAMESID="frame"

OUTPUTDIR="/home/faruk/gdrive/temp_flooding_brains/shots"
OUTPUTID="movie-girafffe_plasma_shot-3"

# -----------------------------------------------------------------------------
# Compile shots using ffmpeg
command="ffmpeg -y "
command+="-i ${FRAMESDIR}/${FRAMESID}-%03d.png "
command+="-vb 20M -c:v libx264 -vf fps=24 -pix_fmt yuv420p "
command+="${OUTPUTDIR}/${OUTPUTID}.mp4"
echo command
${command}

echo "Finished."
