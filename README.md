# 🎮 Rock-Paper-Scissors Game

A classic Rock-Paper-Scissors game built with Python, featuring score tracking, round management, and an interactive command-line interface.

## 📋 Description

This Python implementation of the timeless Rock-Paper-Scissors game allows users to play against the computer with comprehensive score tracking, multiple rounds, and detailed game statistics. The game follows the traditional rules where:
- 🪨 Rock beats ✂️ Scissors
- ✂️ Scissors beats 📄 Paper  
- 📄 Paper beats 🪨 Rock

The game features a clean command-line interface with emoji support, round-by-round tracking, and detailed winner/loser announcements.

## ✨ Features

- 🎯 **Interactive Gameplay**: Play Rock-Paper-Scissors against the computer
- 📊 **Score Tracking**: Automatic tracking of wins, losses, and ties
- 🔄 **Multiple Rounds**: Play as many rounds as you want
- 🏆 **Winner Determination**: Clear announcement of each round's winner and loser
- 📈 **Statistics**: View game statistics including win percentages
- ✅ **Input Validation**: Ensures only valid choices are accepted
- 🎨 **Visual Appeal**: Colorful console output with emojis
- 🔄 **Play Again Option**: Continue playing without restarting
- 📝 **Game Summary**: Final results with overall winner announcement

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rock-paper-scissors-game.git
cd rock-paper-scissors-game
```

2. Run the game:
```bash
RPS Game.py
```

## 🎮 How to Play

1. **Start the game**: Run the Python script
2. **Enter your move**: Type "Rock", "Paper", or "Scissors" when prompted
3. **View results**: See the computer's choice and the round result
4. **Check scores**: View updated scores after each round
5. **Continue playing**: Choose to play another round or quit
6. **Final results**: See overall statistics when you finish playing

## 📁 Project Structure

```
rock-paper-scissors-game/
│
├── rock_paper_scissors.py  # Main game file
├── README.md               # This file
├── LICENSE                 # License file
└── requirements.txt        # Python dependencies (none required)
```

## 💻 Code Overview

The game includes:

- **Score Tracking**: `user_wins`, `computer_wins`, `ties` variables
- **Game Loop**: Continuous gameplay until user chooses to quit
- **Input Validation**: Ensures only valid moves are accepted
- **Random Computer Choice**: Uses Python's `random` module
- **Result Calculation**: Logic to determine winner based on game rules
- **Display Functions**: Formatted output for game results and statistics

## 🔧 Customization

You can easily customize the game:

- Change emojis or text formatting
- Modify winning rules
- Add new features like time limits or difficulty levels
- Implement a graphical user interface (GUI)
- Add multiplayer functionality

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the classic hand game
- Built with Python's standard libraries
- Thanks to all contributors and testers

## 📊 Sample Game Output

```
🎮 Welcome to Rock-Paper-Scissors Game! 🎮
==================================================

🔄 ROUND 1
------------------------------
Enter your move (Rock, Paper, Scissor): Rock

🎯 Your choice: Rock
💻 Computer choice: Scissor
🪨 Rock smashes Scissor = You win!
🏆 Winner: You
😞 Loser: Computer

📊 Round 1 Summary:
   Winner: You
   Loser: Computer

📈 OVERALL SCORE (after 1 rounds):
   Your wins: 1
   Computer wins: 0
   Ties: 0
```

## 🎯 Future Enhancements

Planned features for future releases:
- [ ] Graphical User Interface (GUI)
- [ ] Online multiplayer mode
- [ ] Tournament bracket system
- [ ] Player profiles and statistics
- [ ] Sound effects
- [ ] Visual animations
- [ ] Mobile app version

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the existing issues for solutions

---

⭐ **Star this repository if you find it useful!** ⭐

Enjoy the game! 🎮🪨📄✂️
