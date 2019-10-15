-include ./path.mak

# User Defined Variables
CC := $(LINUXarm_GCC)
CFLAGS := -g
LINKER_FLAGS := -lstdc++

all: app.arm

app.arm: app.o
	$(CC) $(CFLAGS) $(LINKER_FLAGS) $^ -o $@
	@echo; echo $@ successfully create; echo

app.o: app.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm app.o app.arm
	
test:
	@echo CC = $(CC)
