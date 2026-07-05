def show_hangman(stage):
    """
    Draw hangman based on the stage number.
    stage: 1, 2, 3...
    """

    drawings = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
    ]

    # Make sure stage stays within the list range
    stage = max(1, min(stage, len(drawings)))

    print(drawings[stage - 1])
