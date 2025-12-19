---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/install-windowsfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Install-WindowsFeature
---

# 安装 Windows 功能

## 摘要
在运行 Windows Server 2012 R2 的本地服务器或指定的远程服务器上安装一个或多个角色、角色服务或功能。

## 语法

### ComponentNamesAndRunningComputer（默认设置）
```
Install-WindowsFeature [-Name] <Feature[]> [-Restart] [-IncludeAllSubFeature] [-IncludeManagementTools]
 [-Source <String[]>] [-ComputerName <String>] [-Credential <PSCredential>] [-LogPath <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ComponentNamesAndVhdPath
```
Install-WindowsFeature [-Name] <Feature[]> -Vhd <String> [-IncludeAllSubFeature] [-IncludeManagementTools]
 [-Source <String[]>] [-ComputerName <String>] [-Credential <PSCredential>] [-LogPath <String>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### ConfigurationFile
```
Install-WindowsFeature -ConfigurationFilePath <String> [-Vhd <String>] [-Restart] [-Source <String[]>]
 [-ComputerName <String>] [-Credential <PSCredential>] [-LogPath <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Install-WindowsFeature` cmdlet 可以在运行 Windows Server 2012 R2 的计算机上，或者在安装了 Windows Server 2012 R2 的离线虚拟硬盘（VHD）上，安装指定的 `rrsandfplural` 组件。该 cmdlet 与用于在 Windows Server 2008 R2 中安装角色、角色服务和组件的 `Add-WindowsFeature` cmdlet 功能相同，并且可以替代后者。

这个 cmdlet 的使用方式与 Server Manager 中的 `arfw` 类似，但有一个重要的区别：默认情况下，该 cmdlet 不会安装与 `rrsandfplural` 组件相关的管理工具。如果需要在目标服务器上安装这些管理工具（例如插件），必须在命令中添加 `IncludeManagementTools` 参数。

此cmdlet需要提升权限；您必须以管理员身份运行Windows PowerShell会话才能使用该cmdlet。

## 示例

### 示例 1：在指定的计算机上安装 IIS（包括所有角色服务及相关的管理工具）
```
PS C:\> Install-WindowsFeature -Name "Web-Server" -IncludeAllSubFeature -IncludeManagementTools -ComputerName "Server1" -Credential "contoso.com\PattiFul"
```

该命令使用名为 contoso.com\PattiFul 的用户账户的凭据，在名为 Server1 的计算机上安装 Web 服务器（IIS），包括所有的角色服务及相应的管理工具。

### 示例 2：从配置文件中将所有角色服务及相关管理工具安装到默认计算机上
```
PS C:\> Install-WindowsFeature -ConfigurationFilePath "d:\ConfigurationFiles\ADCSConfigFile.xml"
```

该命令会安装配置文件 `ADCSConfigFile.xml` 中指定的所有角色、角色服务及功能。该配置文件是通过在服务器管理器的 “ARFW”（Aruba Routing Framework）的 “确认安装选项” 页面上点击 “导出配置设置” 生成的。

### 示例 3：根据配置文件的要求，将 Active Directory Domain Services (AD CS) 安装到一组计算机上
```
PS C:\> $Servers = ('server1', 'server2')
PS C:\> foreach ($Server in $Servers) {Install-WindowsFeature -ConfigurationFilePath D:\ConfigurationFiles\ADCSConfigFile.xml -ComputerName $Server}
```

该命令会根据名为 ADCSConfigFile.xml 的配置文件中的指定内容来安装 Active Directory Certificate Services（AD CS）。AD CS 被安装在变量 $Servers 中列出的一组计算机上。这个配置文件是通过在 Server Manager 的“Confirm installation selections”页面上点击“Export configuration settings”生成的。在第一行中，设置了变量 $Servers 的值；在第二行中，会将 ADCSConfigFile.xml 配置文件中的安装指令应用到 $Servers 中列出的每一台服务器上。

### 示例 4：使用搜索字符串获取 Windows 功能列表，然后将结果传递给 Install-WindowsFeatures 命令
```
PS C:\> Get-WindowsFeature -Name "Web-*" | Install-WindowsFeature
```

此命令会检索所有以“Web”开头的Windows功能的列表，然后将生成的列表传递给**Install-WindowsFeature**。执行该cmdlet后，本地计算机上将会安装所有以“Web”开头的功能。

### 示例 5：在本地计算机上安装 IIS，并指定一个包含功能文件的文件夹
```
PS C:\> Install-WindowsFeature -Name "Web-Server" -Source "\\server2\winsxs"
```

此命令会在本地计算机上安装Web服务器（IIS），并指定安装所需的功能文件来自名为Server2的计算机上的winsxs文件夹。本地计算机的账户必须具有对该共享资源的读取权限。

## 参数

### -ComputerName
指定一台远程计算机，该cmdlet将在该计算机上安装一个或多个可用的rrsandfplural程序。此参数仅接受一个计算机名称。如果未添加此参数或未指定任何计算机名称，则默认目标为本地计算机。

该参数的有效值包括：运行 Windows Server 的远程计算机的 NetBIOS 名称、IP 地址或完全限定域名。

要将远程计算机的 IP 地址作为该参数的值，您的命令必须包含 *Credential* 参数。要么该计算机需要配置为使用 HTTPS 协议进行传输，要么必须在本地计算机的 WinRM TrustedHosts 列表中添加该远程计算机的 IP 地址。有关如何将计算机名称添加到 WinRM TrustedHosts 列表中的信息，请参阅 [How to Add a Computer to the Trusted Host List in about_Remote_Troubleshooting](https://go.microsoft.com/fwlink/p/?LinkID=135188)。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ConfigurationFilePath
指定一个配置文件的路径，该文件用于指定要安装的角色和功能以及所需的任何配置参数。路径可以通过使用本地相对路径或使用以 `$env` 标签开头的内置环境变量来指定（例如 $env:systemdrive\filename）。可以在服务器管理器中运行 arfw 命令来生成配置文件。

如果指定了此参数，则无法使用*Name*参数。

```yaml
Type: String
Parameter Sets: ConfigurationFile
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个具有执行此操作所需访问权限的用户账户。如果未添加该参数，或者未指定任何值，则该参数的默认值为当前用户。请以以下格式之一输入用户名（引号可选）。

- UserName
- Domain\User
- User@Domain.com
- A Credential object returned by the Get-Credential cmdlet.

如果用户输入了用户名，系统会显示一个要求输入密码的提示。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeAllSubFeature
表示该cmdlet会安装所有从属的角色服务，以及由*Name*参数指定的父角色、角色服务或功能的所有子特性。

```yaml
Type: SwitchParameter
Parameter Sets: ComponentNamesAndRunningComputer, ComponentNamesAndVhdPath
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IncludeManagementTools
该参数表示此cmdlet会安装由*Name*参数指定的角色、角色服务或功能所对应的所有适用的管理工具。虽然在使用arfw安装功能时管理工具会默认被安装，但使用**Install-WindowsFeature** cmdlet安装功能时管理工具并不会被自动安装；因此必须明确指定该参数才能完成管理工具的安装。

```yaml
Type: SwitchParameter
Parameter Sets: ComponentNamesAndRunningComputer, ComponentNamesAndVhdPath
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogPath
指定日志文件的名称和路径。如果需要将命令的执行结果存储在日志文件中，请添加此参数。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要安装的功能列表。此参数不支持通配符。如果指定了此参数，则无法使用 *ConfigurationFilePath* 参数。

```yaml
Type: Feature[]
Parameter Sets: ComponentNamesAndRunningComputer, ComponentNamesAndVhdPath
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Restart
表示如果指定的角色或功能的安装过程需要重启目标计算机，那么该cmdlet会自动执行重启操作。此参数不能与*Vhd*参数一起使用。

```yaml
Type: SwitchParameter
Parameter Sets: ComponentNamesAndRunningComputer, ConfigurationFile
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Source
指定功能文件的路径。如果这些文件不在目标计算机的本地功能存储库或VHD中，则需要指定该路径。此参数的有效值可以是网络路径，也可以是Windows镜像文件（WIM）的路径。如果您正在离线的VHD上安装角色或功能，必须使用已挂载的WIM文件。在运行中的物理计算机上进行安装时，无需手动挂载WIM文件，因为系统会自动将其内部挂载以完成部署。您可以使用本地相对路径来指定路径，或者使用以 `$env` 为前缀的内置环境变量来指定路径（如下例所示）。

只有当命令无法在指定目标计算机的本地并行存储或VHD中找到功能文件时，才会使用此参数指定的路径。命令会按以下顺序搜索功能文件：

- On the target computer or offline VHD.
- Path specified as the value of this parameter. If you add a Universal Naming Convention (UNC) path, verify that the computer account of the target server has Read permissions on the share. The computer account should be in one of the following formats: DOMAIN\SERVERNAME$ or SERVER$
- Repository path specified by the Group Policy Object (GPO), Specify settings for optional component installation and component repair, located in Computer Configuration/Administrative Templates/System in Local Group Policy Editor. This Group Policy setting controls the following Windows Registry setting: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Servicing\LocalSourcePath.
- Windows Update.

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Vhd
指定离线VHD文件的路径。该路径可以指向VHD文件本身，也可以指向通过“部署映像服务与管理”（Deployment Image Servicing and Management，简称DISM）工具已挂载VHD的所在位置。

VHD可以位于目标计算机的本地磁盘上，也可以位于网络共享文件夹中。如果VHD位于网络共享文件夹中，则该参数的值为指向VHD的UNC路径。在这种情况下，用于挂载VHD的计算机的账户必须具有对该共享文件夹的读写权限（在“文件共享”对话框中选择“读取/写入”权限，或在“文件夹属性”对话框的“安全”选项卡中选择“完全控制”权限），否则将无法访问该VHD。不支持使用本地回环（loopback）UNC路径。计算机账户可以使用以下两种格式之一：DOMAIN\SERVERNAME$ 或 SERVERNAME$.

请添加 *ComputerName* 参数，以指定用于挂载 VHD 的目标计算机。如果未指定 *ComputerName* 参数，则会使用本地计算机。用于挂载 VHD 的计算机必须运行 Windows Server 2012 R2 操作系统。通过该参数指定的任何本地路径（例如 D:\myFolder）始终是相对于目标计算机的。

```yaml
Type: String
Parameter Sets: ComponentNamesAndVhdPath
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: String
Parameter Sets: ConfigurationFile
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Windows.ServerManagerCommands.Feature[]

## 输出

### Microsoft.Windows.ServerManager Commands.FeatureOperationResult

## 备注

## 相关链接

[Get-WindowsFeature](./Get-WindowsFeature.md)

[卸载 Windows 功能](./Uninstall-WindowsFeature.md)

[Enable-ServerManagerStandardUserRemoting](./Enable-ServerManagerStandardUserRemoting.md)

[禁用 ServerManager 标准用户远程访问功能](./ Disable-ServerManagerStandardUserRemoting.md)

