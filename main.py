import click

@click.command()
def main():
	click.echo("Welcome to the CM Banking App!")
	current_account_holder = click.prompt("Do you hold an account with us? (Yes/No)", type=str)
	if current_account_holder.lower() == "yes":
		click.echo("Thank you for being a valued customer!")
	elif current_account_holder.lower() == "no":
		create_account()
	else:
		click.echo("Invalid response. Please answer with 'Yes' or 'No'.")
	
        



def create_account():
	want_new_account = click.prompt('Would you like to create an account with us? (Yes/No)')
	if want_new_account == 'yes':
		create_name = click.prompt("Please enter your name", type=str)
		create_name = check_name(create_name)
		create_email = click.prompt("Please enter your email", type=str)
		create_email = check_email(create_email)
		create_passoword = click.prompt("Please create a password", type=str)
		create_passoword = passowrd_check(create_passoword)
		create_pin =  click.prompt('Please create a 4-digit PIN', type=int, default='0000')
		create_pin = pin_check(create_pin)
		click.echo(f"Account created successfully for {create_name} with email {create_email}. Your PIN is {create_pin}.")



def check_name(create_name):
	while len(create_name) < 3 or len(create_name)  > 50:
		click.echo("Name must be between 3 and 50 characters.")
		create_name = click.prompt("Please enter your name", type=str)
	return create_name

def check_email(create_email):
    while '@' not in create_email or '.' not in create_email:
        click.echo("Invalid email format. Please try again.")
        create_email = click.prompt("Please enter your email", type=str)
    return create_email

def passowrd_check(create_passoword):
    while len(create_passoword) < 8 or len(create_passoword) > 20 and not any(char in '!@#$%^&*()_+' for char in create_passoword):
        click.echo("Password must be between 8 and 20 characters.")
        create_passoword = click.prompt("Please create a password", type=str)
    return create_passoword
		
def pin_check(create_pin):
	while create_pin > 9999 or create_pin < 0000 and create_pin.isdigit():
		click.echo("PIN must be exactly 4 digits.")
		create_pin = click.prompt('Please create a 4-digit PIN', type=int, default='0000')
	return create_pin


 



if __name__ == "__main__":
	main()
