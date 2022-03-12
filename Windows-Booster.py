import subprocess
import os
import winreg
import shutil

import colorama
from colorama import Fore

colorama.init()

from art import tprint

tprint('Windows Booster V1.1')

REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"


def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                      winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False


def set_reg_current_user(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                      winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False


def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                      winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


def get_reg_current_user(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                      winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


set_reg('EnableLUA', 0)

print(Fore.GREEN + "NEXT UPDATE: 1.5 NVIDIA PROFILE IMPORTER FOR GAME FPS (maybe idk) AND DRIVER UPDATER :0")


def menu():
    print(Fore.BLUE + "[1] Import optimized Power Plan")
    print("[2] Delete Temp Files (May take a while)")
    print("[3] Delete Log Files (May take a while)")
    print("[4] Turn Off Power Throttling")
    print("[5] Keyboard and Mouse tweaks")
    print("[6] Latency Tweaks")
    print("[7] Best GameUserSettings for Fortnite")
    print("[8] AMD Radeon Tweaks")
    print(Fore.RED + "[0] Exit")
    print(Fore.RESET + " ")

    # OK OK so all the people looking through the code and saying "What the fuck is this kid doing??"
    # Im using fore.reset on an empty string cause cmd didn't like it on an input so yeah. I bet theres another way to do it but i just did that lol


menu()

option = int(input("Choose an option: "))

while option != 0:
    if option == 1:
        line = os.path.abspath("Power Plan/PowerPlan.pow")
        powercfg = subprocess.call(["powercfg", "-import", line], shell=True)
        print("\nDone!")
    elif option == 2:
        os.system(
            'takeown /f "%temp%" /r /d y & RD /S /Q %temp% & MKDIR %temp% & takeown /f "%temp%" /r /d y & takeown /f '
            '"C:\Windows\Temp" /r /d y & RD /S /Q C:\Windows\Temp & MKDIR C:\Windows\Temp & takeown /f '
            '"C:\Windows\Temp" /r /d y')
        print("\nDone!")
    elif option == 3:
        os.system("cd C:/ & del *.log /a /s /q /f")
        print("\nDone!")
    elif option == 4:
        REG_PATH = r"SYSTEM\CurrentControlSet\Control\Power\PowerThrottling"
        set_reg('PowerThrottlingOff', 1)
        print("Done!")
    elif option == 5:
        # Keyboard Reg
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\kbdclass\Parameters"
        set_reg('KeyboardDataQueueSize', 14)
        print("Keyboard Tweak Finished")

        # Mouse Reg
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\mouclass\Parameters"
        set_reg('MouseDataQueueSize', 14)
        print("Mouse Tweak Finished")
        print("Done!")
    elif option == 6:
        REG_PATH = r"SYSTEM\CurrentControlSet\Control\PriorityControl"
        set_reg('ConvertibleSlateMode', 0)
        set_reg('Win32PrioritySeparation', 28)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\DiagTrack"
        set_reg('Start', 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\dmwappushservice"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\diagsvc"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\DPS"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\diagnosticshub.standardcollector.service"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\WdiServiceHost"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\WdiSystemHost"
        set_reg('Start', 4)
        REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications"
        set_reg_current_user('GlobalUserDisabled', 1)
        REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Search"
        set_reg_current_user('BackgroundAppGlobalToggle', 0)
        REG_PATH = r"System\GameConfigStore"
        set_reg_current_user("GameDVR_Enabled", 0)
        set_reg_current_user("GameDVR_FSEBehaviorMode", 2)
        set_reg_current_user("GameDVR_HonorUserFSEBehaviorMode", 0)
        set_reg_current_user("GameDVR_DXGIHonorFSEWindowsCompatible", 1)
        set_reg_current_user("GameDVR_EFSEFeatureFlags", 0)
        REG_PATH = r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR"
        set_reg("value", 0)
        REG_PATH = r"SOFTWARE\Policies\Microsoft\Windows\GameDVR"
        set_reg("AllowGameDVR", 0)
        REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\GameDVR"
        set_reg_current_user("AppCaptureEnabled", 0)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\GpuEnergyDrv"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\MapsBroker"
        set_reg("Start", 4)
        REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        set_reg_current_user("EnableTransparency", 0)
        REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\DriverSearching"
        set_reg("SearchOrderConfig", 0)
        REG_PATH = r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowSharedUserAppData"
        set_reg("value", 0)
        REG_PATH = r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowStore"
        set_reg("value", 0)
        REG_PATH = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance"
        set_reg("MaintenanceDisabled", 1)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\XblGameSave"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\XboxNetApiSvc"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\XboxGipSvc"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Services\XblAuthManager"
        set_reg("Start", 4)
        REG_PATH = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
        set_reg("FeatureSettingsOverride", 3)
        set_reg("FeatureSettingsOverrideMask", 3)

        print("Done!")
        choice = input(
            "All the tweaks have been applied. Please restart your computer for the changes to fully take effect (y or n) : ")

        if choice == "y" or choice == "Y":
            os.system("shutdown /r /t 1")

        else:
            menu()
    elif option == 7:
        print(Fore.BLUE + "[1] Low End/Competitive (Performance Mode) (BEST FPS)")
        print("[2] Medium End (DX11) Low/Medium Graphics")
        print("[3] High End (DX12) Medium/High Graphics")
        print(
            "[4] SUPER MEGA LOAD (DX12) RAYTRACING AND CRAZY GRAPHICS (30-120 fps) " + Fore.RED + "DO NOT USE IF YOU DON'T HAVE AN RTX CARD!")
        print(Fore.RESET + " ")

        option_settings = int(input("Choose your option: "))

        if option_settings == 1:
            original = r"GameUserSettings\1 Low End.ini"
            target = r"C:\Users\Zaydin\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini"

            shutil.copyfile(original, target)

            print("Done!")
        elif option_settings == 2:
            original = r"GameUserSettings\2 Medium End.ini"
            target = r"C:\Users\Zaydin\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini"

            shutil.copyfile(original, target)

            print("Done!")

        elif option_settings == 3:
            original = r"GameUserSettings\3 High End.ini"
            target = r"C:\Users\Zaydin\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini"

            shutil.copyfile(original, target)

            print("Done!")

        elif option_settings == 4:
            original = r"GameUserSettings\4 Why.ini"
            target = r"C:\Users\Zaydin\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini"

            shutil.copyfile(original, target)

            print("Done!")
        else:
            print("Invalid Option.")
    elif option == 8:
        REG_PATH = r'SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000'
        set_reg("EnableUlps", 0)
        REG_PATH = r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\UMD"
        set_reg("Tessellation_OPTION", 32)
        set_reg("Tessellation", 31)
        set_reg("TFQ", 32)
        
    else:
        print("Invalid option.")
    print()
    menu()
    option = int(input("Choose an option: "))

print("Thanks for using this program. goodbye!")
