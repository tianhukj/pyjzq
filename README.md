# pyjzq

![Build Status](https://github.com/tianhukj/pyjzq/actions/workflows/python-package.yml/badge.svg)
![License](https://img.shields.io/github/license/tianhukj/pyjzq)
![PyPI](https://img.shields.io/pypi/v/pyjzq)

这是一个基于命令行的井字棋游戏。

## 安装

```bash
pip install pyjzq
```

## 使用方法
在Python代码中使用
你可以在Python代码中导入并使用这个包。以下是一个简单的示例：

```
from pyjzq import TicTacToe, play

# 创建游戏实例
game = TicTacToe()

# 开始游戏
play(game, 'X', 'O')
```

## 示例输出
以下是运行上述代码时的示例输出：

```
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

X makes a move to square 0
| X |   |   |
|   |   |   |
|   |   |   |

O makes a move to square 1
| X | O |   |
|   |   |   |
|   |   |   |

...

X wins!
```
