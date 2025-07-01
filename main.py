import click

@click.command()
def main():
	click.echo("Welcome to the CM Banking App!")
	current_account_holder = click.prompt("Do you hold an account with us? (Yes/No)", type=str)
	if current_account_holder.lower() == "yes":
		click.echo("Thank you for being a valued customer!")
	elif current_account_holder.lower() == "no":
		click.echo("Create account")
	else:
		click.echo("Invalid response. Please answer with 'Yes' or 'No'.")
	
        













if __name__ == "__main__":
	main()
