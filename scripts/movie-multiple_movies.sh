
ID="movie-dolphin_black"

# -----------------------------------------------------------------------------
# Compile shots
ffmpeg -y -i frames/${ID}_shot-1/frame-%03d.png -vb 20M -c:v libx264 -vf fps=24 -pix_fmt yuv420p shots/${ID}_shot-1.mp4

ffmpeg -y -i frames/${ID}_shot-2/frame-%03d.png -vb 20M -c:v libx264 -vf fps=24 -pix_fmt yuv420p shots/${ID}_shot-2.mp4

ffmpeg -y -i frames/${ID}_shot-3/frame-%03d.png -vb 20M -c:v libx264 -vf fps=24 -pix_fmt yuv420p shots/${ID}_shot-3.mp4

# Final cut
ffmpeg -y -f concat -i shots/${ID}_repeatlist.txt -c copy ${ID}.mp4

# Convert to gif
ffmpeg -y -i ${ID}.mp4 -vf "fps=24, scale=360:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 ${ID}.gif
