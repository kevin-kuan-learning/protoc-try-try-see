set SRC_DIR=.
set DST_DIR=.
..\bin\protoc -I=%SRC_DIR% --python_out=%DST_DIR% %SRC_DIR%/addressbook.proto
