def update_progress(
        progress: float,
        bar_length: int = 20,
        time_elapsed: str = "") -> None:
    """
    Prints progress bar at current progress level

    Args:
    progress (float): Current progress represented as a float between 0 and 1
    bar_length (int): Desired length of progress bar
    """

    progress = _clean_input(progress)
    completed_length = int(round(progress * bar_length))
    remaining_length = bar_length - completed_length

    completed_block = "=" * completed_length
    remaining_block = "-" * remaining_length
    percent_complete = round(progress * 100, 2)
    formatted_time_elapsed = _format_time_elapsed(time_elapsed)

    output = f"\rProgress: [{completed_block}{remaining_block}] {percent_complete}% {formatted_time_elapsed} "

    print(output, flush=True, end="")

    if progress == 1:
        print(f"\nComplete in {formatted_time_elapsed}", flush=True)


def _clean_input(input) -> float:
    """
    Validates and cleans input, returns float of input
    """
    if isinstance(input, int):
        input = float(input)
    if not isinstance(input, float):
        raise TypeError()
    
    return input


def _format_time_elapsed(time_elapsed) -> str:
    if time_elapsed >= 60:
        minutes, seconds = divmod(time_elapsed, 60)
        return f"{minutes} minutes {"{:.2f}".format(seconds)} seconds"

    return f"{"{:.2f}".format(time_elapsed)} seconds"