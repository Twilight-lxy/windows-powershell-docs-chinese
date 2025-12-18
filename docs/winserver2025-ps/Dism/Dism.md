---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.1.1
Locale: en-US
Module Guid: 389c464d-8b8d-48e9-aafe-6d8a590d6798
Module Name: Dism
ms.date: 10/07/2021
title: Dism Module
---

# Dism 模块

## 说明

部署映像服务与管理（DISM）平台用于在部署之前挂载和管理Windows映像。部分DISM命令可以在在线的Windows映像上使用。您可以使用DISM工具来挂载Windows映像文件（`.wim`）或虚拟硬盘文件（`.vhd` 或 `.vhdx`），并获取相关信息。此外，还可以利用该工具在Windows映像中安装、卸载、配置和更新Windows功能、组件及驱动程序，或者更改Windows映像的版本。

DISM平台还包括一个命令行工具 `dism.exe`，以及 [DISM API](https://go.microsoft.com/fwlink/?LinkID=237611)。该命令行工具包含在 [Windows评估和部署工具包（Windows ADK）](https://go.microsoft.com/fwlink/?LinkId=206587) 中，提供了额外的功能，以支持针对国际设置的服务相关操作。

在运行 Dism cmdlets 时，你可以通过检查 `$?` 变量的值来判断是否出现了错误。如果该变量的值为 True，则表示上一次操作成功；如果值为 False，则表示上一次操作失败。`$LASTEXITCODE` 变量则存储了最近执行的 Win32 可执行文件的退出代码。例如，要检查 `Get-WindowsImage` cmdlet 是否无法获取文件 `E:\images\c.wim` 中包含的 Windows 镜像的相关信息，可以输入以下命令：

```powershell
try
{

    Get-WindowsImage -ImagePath E:\images\c.wim
}
catch
{
    $message = "TRAPPED: {0}: '{1}'" -f ($_.Exception.GetType().FullName), ($_.Exception.Message)
    Write-host $message
}
```

有关错误处理的更多信息，请参阅[about_Try_Catch_Finally](https://go.microsoft.com/fwlink/p/?LinkID=317390)。

## Dism Cmdlets
### [Add-AppxProvisionedPackage](./Add-AppxProvisionedPackage.md)
将一个应用程序包（.appx）添加到Windows镜像中，该程序包会在每个新用户登录时自动安装。

### [Add-WindowsCapability](./Add-Windows Capability.md)
在指定的操作系统镜像上安装一个 Windows 功能包。

### [Add-WindowsDriver](./Add-WindowsDriver.md)
向一个离线的Windows镜像中添加驱动程序。

### [Add-WindowsImage](./Add-WindowsImage.md)
向现有的图像文件（.wim）中添加另一张图片。

### [Add-WindowsPackage](./Add-WindowsPackage.md)
将一个 `.cab` 或 `.msu` 文件添加到 Windows 镜像中。

### [清除损坏的Windows挂载点](./Clear-WindowsCorruptMountPoint.md)
删除与已损坏的挂载镜像相关的所有资源。

### [禁用 Windows 可选功能](./ Disable-WindowsOptionalFeature.md)
禁用Windows镜像中的某个功能。

### [Dismount-WindowsImage](./Dismount-WindowsImage.md)
从映射到的目录中卸载Windows镜像文件。

### [Enable-WindowsOptionalFeature](./Enable-WindowsOptionalFeature.md)
用于启用Windows镜像中的某个功能。

### [Expand-WindowsCustomDataImage](./Expand-WindowsCustomDataImage.md)
用于扩展自定义数据图像。

### [Expand-WindowsImage](./Expand-WindowsImage.md)
将一张图片应用到指定的位置。

### [Export-Windows CapabilitySource](Export-WindowsCapabilitySource.md)
创建一个自定义的FOD（Fixed Operating Distribution）仓库，其中包含支持安装指定功能的软件包。

### [Export-WindowsDriver](Export-WindowsDriver.md)
将Windows镜像中的所有第三方驱动程序导出到目标文件夹中。

### [Export-WindowsImage](./Export-WindowsImage.md)
将指定的图像复制并导出到另一个图像文件中。

### [Get-AppxProvisionedPackage](./Get-AppxProvisionedPackage.md)
获取关于应用程序包（.appx）的信息，这些应用程序包将随新用户安装的图像一起被提供给用户。

### [Get-NonRemovableAppsPolicy](Get-NonRemovableAppsPolicy.md)
返回一个列表，其中包含已安装并配置为不可移除应用程序的应用程序包。

### [Get-WIMBootEntry](Get-WIMBootEntry.md)
显示指定磁盘卷的 Windows 映像文件启动（WIMBoot）配置项。

### [Get-WindowsCapability](./Get-WindowsCapability.md)
为图像或正在运行的操作系统获取Windows系统的相应功能/支持。

### [Get-WindowsDriver](./Get-WindowsDriver.md)
显示有关Windows镜像中驱动程序的信息。

### [Get-WindowsEdition](./Get-WindowsEdition.md)
获取有关Windows镜像的版本信息。

### [Get-WindowsImage](./Get-WindowsImage.md)
获取关于 WIM 或 VHD 文件中 Windows 镜像的信息。

### [Get-WindowsImageContent](./Get-WindowsImageContent.md)
显示指定图像中的文件和文件夹列表。

### [Get-WindowsOptionalFeature](./Get-WindowsOptionalFeature.md)
获取有关Windows镜像中可选功能的信息。

### [Get-WindowsPackage](./Get-WindowsPackage.md)
获取有关Windows镜像中包的信息。

### [Get-WindowsReservedStorageState](./Get-WindowsReservedStorageState.md)
获取图像的预留存储状态。

### [Mount-WindowsImage](./Mount-WindowsImage.md)
将Windows镜像（位于WIM或VHD文件中）安装到本地计算机的某个目录中。

### [New-WindowsCustomImage](./New-WindowsCustomImage.md)
在配置了 Windows 图像文件启动（WIMBoot）功能的设备上，捕获自定义或经过维护的 Windows 组件的图像。

### [New-WindowsImage](./New-WindowsImage.md)
将驱动器的图像捕获到一个新的WIM文件中。

### [优化 AppXProvisionedPackages](Optimize-AppXProvisionedPackages.md)
通过用硬链接替换重复的文件来优化镜像中已配置包的总文件大小。

### [优化Windows镜像](Optimize-WindowsImage.md)
配置一个包含指定优化设置的Windows镜像文件。

### [Remove-AppxProvisionedPackage](./Remove-AppxProvisionedPackage.md)
从Windows镜像中删除一个应用程序包（.appx）。

### [Remove-WindowsCapability](./Remove-WindowsCapability.md)
从镜像中卸载一个Windows功能包。

### [Remove-WindowsDriver](./Remove-WindowsDriver.md)
从离线的Windows镜像中删除某个驱动程序。

### [Remove-WindowsImage](./Remove-WindowsImage.md)
从一个包含多个卷图像的WIM文件中删除指定的卷图像。

### [Remove-WindowsPackage](./Remove-WindowsPackage.md)
从Windows镜像中删除一个软件包。

### [修复Windows镜像](./Repair-WindowsImage.md)
修复 WIM 或 VHD 文件中的 Windows 镜像。

### [Save-WindowsImage](./Save-WindowsImage.md)
将对已挂载的镜像所做的更改应用到其WIM或VHD文件中。

### [Set-AppXProvisionedDataFile](./Set-AppXProvisionedDataFile.md)
将自定义数据添加到已配置在 Windows 镜像中的指定应用程序（.appx）包中。

### [Set-NonRemovableAppsPolicy](Set-NonRemovableAppsPolicy.md)
将某个应用程序包设置为“不可移除”状态（即无法卸载该应用）。

### [Set-WindowsEdition](Set-WindowsEdition.md)
将Windows镜像版本升级到更高版本。

### [Set-WindowsProductKey](./Set-WindowsProductKey.md)
为Windows镜像设置产品密钥。

### [Set-WindowsReservedStorageState](./Set-WindowsReservedStorageState.md)
设置图像的预留存储状态。

### [Split-WindowsImage](./Split-WindowsImage.md)
将现有的.wim文件分割成多个只读的单独.wim文件。

### [开始卸载操作系统](Start-OSUninstall.md)
Windows 允许用户卸载软件或将系统恢复到之前的版本。你可以使用 DISM 来启动卸载过程。

### [更新 WIM 启动条目](Update-WIMBootEntry.md)
更新与指定的数据源ID、重命名的镜像文件路径或移动后的镜像文件路径相关联的Windows镜像文件引导（WIMBoot）配置项。

### [Use-WindowsUnattend](./Use-WindowsUnattend.md)
将一个无人值守的回答文件应用到Windows镜像上。
