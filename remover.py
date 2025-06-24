import demucs.separate

print("----Type----")
print("1. drums \n" 
"2. bass \n" 
"3. other \n" 
"4. vocals")
print("------------")
type = int(input("분리할 타입을 선택해 주세요: "))
file_name = input("분리할 파일명을 입력해 주세요: ")

if int(type) == 1:
   type = "drums"
elif int(type) == 2:
   type = "bass"
elif int(type) == 3:
   type = "other"
elif int(type) == 4:
   type = "vocals"

print("please wait...")
demucs.separate.main(["--mp3", "--mp3-bitrate", "320", "--two-stems", f"{type}", "-n", "mdx_extra", f"{file_name}.mp3"])
print("done.")