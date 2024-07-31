// This is a simple login program in C++
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> usernames = { "admin" };
    std::vector<std::string> passwords = { "123456" };
    int remainingAttempts = 0;

    while (remainingAttempts < 4) {
        std::string inputUsername;
        std::cout << "请输入你的账号（若没有账号请输入“注册”）：";
        std::cin >> inputUsername;

        auto it = std::find(usernames.begin(), usernames.end(), inputUsername);
        if (it != usernames.end()) {
            int index = std::distance(usernames.begin(), it);
            std::string inputPassword;
            std::cout << "请输入你的密码：";
            std::cin >> inputPassword;
            std::string correctPassword = passwords[index];

            if (inputPassword == correctPassword) {
                std::cout << "登录成功" << std::endl;
                break;
            }
            else {
                remainingAttempts++;
                if (remainingAttempts != 4) {
                    std::cout << "登录错误，你还有 " << 4 - remainingAttempts << " 次机会" << std::endl;
                    continue;
                }
                else {
                    std::cout << "登录失败，程序锁定" << std::endl;
                }
            }
        }
        else if (inputUsername == "注册") {
            std::string newUsername;
            std::string newPassword;
            std::cout << "请输入新账号：";
            std::cin >> newUsername;
            std::cout << "请输入新密码：";
            std::cin >> newPassword;
            usernames.push_back(newUsername);
            passwords.push_back(newPassword);
            std::cout << "注册成功" << std::endl;
        }
        else {
            std::cout << "找不到你的账号，请重新输入" << std::endl;
        }
    }

    return 0;
}