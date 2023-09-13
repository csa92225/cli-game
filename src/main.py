import click
import json
import questionary
import time

from threading import Timer
from random import randint


class QuestionaryOption(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)
        if not isinstance(self.type, click.Choice):
            raise Exception("ChoiceOption type arg must be click.Choice")

    def prompt_for_value(self, ctx):
        val = questionary.select(self.prompt, choices=self.type.choices).unsafe_ask()
        return val


@click.command()
@click.pass_context
@click.option("--topic", "-s", prompt="Choose the game topic", type=click.Choice(["country", "fruit", "state"], case_sensitive=False), cls=QuestionaryOption)
@click.option("--level", "-l", prompt="Choose the level of difficulty", type=click.Choice(["easy", "medium", "hard"], case_sensitive=False), cls=QuestionaryOption)
def wordmaster_challenge_game(ctx, topic, level):
    """Simple game to compete who can list the most words related to a chosen topic."""

    with open("../data.json") as json_file:
        global TIMED_OUT
        TIMED_OUT = False

        # Retrieve relevant dataset for the selected topic
        objects = json.load(json_file)[topic]

        # # of times that PC will answer
        game_cycle = randint(3, 10)

        # PC's inputs will come from a random selection of words in the dataset
        pc_inputs = []
        for i in range(20):
            pc_inputs.append(objects[randint(1, 40)])

        inputs = []
        game_over = False

        while not game_over:

            #  Set a timer based on the chosen difficulty level
            seconds = set_timeout(level)
            t = Timer(seconds, time_out, [", ".join(inputs)])
            t.start()

            value = input(f"Enter your {topic}: ").lower().strip()

            # When the time runs out, the game ends
            if TIMED_OUT == True:
                if click.confirm("Play one more round?"):
                    time.sleep(1)
                    print("")
                    ctx.invoke(wordmaster_challenge_game())
                break

            # If a value is received in time, stop the timer
            t.cancel()

            # If a user's input is not related to the topic, end the game
            if value not in objects:
                game_over = True
                click.secho("-----GAME OVER-----", bg="red")
                click.echo(f'"{value}" is not a {topic}')
                click.echo(
                    f"Previously entered words: "
                    + click.style(", ".join(inputs) if inputs else "", fg="yellow")
                )

                # Restart the game
                if click.confirm("Play one more round?"):
                    return ctx.invoke(wordmaster_challenge_game())
                break

            # End the game if the user enters a value that was previously entered
            elif value in inputs:
                game_over = True
                click.secho("-----GAME OVER-----", bg="red")
                click.echo(f"{value} was already entered")
                click.echo(
                    f"Previously entered words: "
                    + click.style(", ".join(inputs), fg="yellow")
                )

                if click.confirm("Play one more round?"):
                    ctx.invoke(wordmaster_challenge_game())
                break

            else:
                # When the PC loses
                if game_cycle < 1:
                    click.echo("Dr.Brain is thinking.....")
                    time.sleep(2)
                    click.secho(
                        "Uh oh, Dr. Brain is stumped and can't come up with the next word!.........",
                        fg="blue",
                    )
                    time.sleep(2)
                    click.secho("YOU WON!!!!!", fg="yellow", blink=True, bold=True)
                    click.echo(
                        f"Previously entered words: "
                        + click.style(", ".join(inputs), fg="yellow")
                    )

                    if click.confirm("Play one more round?"):
                        ctx.invoke(wordmaster_challenge_game())
                    break

                else:
                    # Get the pc's input from a randomly generated list
                    for i in range(20):
                        pc_value = pc_inputs[i]
                        # Skip the value that has been entered before
                        if pc_value in inputs:
                            continue

                        else:
                            time.sleep(0.5)
                            click.echo("Dr.Brain is thinking.....")
                            time.sleep(1.5)
                            click.echo(
                                "Dr.Brain entered: "
                                + click.style(pc_value, fg="blue")
                            )
                            inputs.append(pc_value)
                            inputs.append(value)
                            game_cycle -= 1
                            break


def time_out(inputs):
    print("")
    global TIMED_OUT
    TIMED_OUT = True

    click.secho("!!!!!!!! TIME OUT !!!!!!!!", fg="yellow", blink=True)
    click.secho("--------- GAME OVER ---------", bg="red")
    click.echo(
        f"Previously entered words: "
        + click.style(inputs if inputs else "", fg="yellow")
    )
    click.echo(f'Press "Enter" to continue........')


def set_timeout(level):
    if level == "hard":
        return 3
    elif level == "medium":
        return 6
    else:
        return 10


if __name__ == "__main__":
    wordmaster_challenge_game()
