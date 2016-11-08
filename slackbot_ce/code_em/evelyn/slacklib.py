# Put your commands here
COMMAND1 = "What is your name?

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I'm Piebot! Im a awesome robot who loves pie!"
        
    return response

