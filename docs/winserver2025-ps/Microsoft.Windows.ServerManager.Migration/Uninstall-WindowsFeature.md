---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/uninstall-windowsfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-WindowsFeature
---

# 卸载 Windows 功能

## 摘要
从运行Windows Server 2012 R2的计算机上卸载指定的Windows Server角色、角色服务以及相关功能。

## 语法

### 运行计算机（默认设置）
```
Uninstall-WindowsFeature [-Name] <Feature[]> [-Restart] [-IncludeManagementTools] [-Remove]
 [-ComputerName <String>] [-Credential <PSCredential>] [-LogPath <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VhdPath
```
Uninstall-WindowsFeature [-Name] <Feature[]> [-Vhd <String>] [-IncludeManagementTools] [-Remove]
 [-ComputerName <String>] [-Credential <PSCredential>] [-LogPath <String>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Uninstall-WindowsFeature` cmdlet 可以卸载指定的角色、角色服务及功能，这些组件可以位于运行 Windows Server 2012 R2 的计算机上，也可以位于安装了 Windows Server 2012 R2 的离线虚拟硬盘（VHD）中。通过添加 `*Remove` 参数，该 cmdlet 还会从计算机上卸载相应的功能文件或相关数据。这个 cmdlet 替代了在 Windows Server 2008 R2 中用于卸载角色、角色服务的 `Uninstall-WindowsFeature` cmdlet。

该 cmdlet 的使用方式与 Server Manager 中的 rrfw 类似，但有一个重要区别：默认情况下，运行 `Uninstall-WindowsFeature` cmdlet 时不会卸载相关的管理工具；如果需要卸载这些管理工具，必须添加 `*IncludeManagementTools` 参数。

此cmdlet需要提升权限；您必须以管理员身份运行Windows PowerShell会话才能使用该cmdlet。

## 示例

### 示例 1：卸载目标服务器上安装的各种角色和功能
```
PS C:\> Get-WindowsFeature | Where-Object -FilterScript { $_.Installed -Eq $TRUE } | Uninstall-WindowsFeature
```

此命令会卸载目标服务器上当前已安装的所有角色或功能。

### 示例 2：从指定的服务器中删除所有角色服务
```
PS C:\> Uninstall-WindowsFeature -Name "Web-Server" -ComputerName "Server1" -Credential "contoso\user1"
```

此命令会从 Server1 上卸载 Web 服务器（IIS），同时移除所有相关的角色服务。执行该操作的用户名是 contoso\user1。

### 示例 3：移除本地服务器上未安装的角色或功能对应的配置文件
```
PS C:\> Get-WindowsFeature | Where-Object -FilterScript { $_.Installed -Eq $FALSE } | Uninstall-WindowsFeature -Remove
```

此命令会删除本地服务器上尚未安装的任何角色或功能所对应的配置文件（即特征文件）。

## 参数

### -ComputerName
指定此cmdlet要卸载程序的远程计算机，并可选地删除一个或多个rrsandfplural文件。该参数仅接受一个计算机名称。如果未添加此参数或未指定任何计算机名称，则默认目标为本地计算机。

该参数的有效值包括：运行Windows Server的远程计算机的NetBIOS名称、IP地址或完全 Qualified Domain Name（FQDN）。

要将远程计算机的 IP 地址作为此参数的值，您的命令必须包含 *Credential* 参数。该计算机必须配置为使用 HTTPS 协议进行通信，或者远程计算机的 IP 地址必须被添加到本地计算机的 WinRM TrustedHosts 列表中。有关如何将计算机名称添加到 WinRM TrustedHosts 列表中的信息，请参阅 [如何在 about_Remote_Troubleshooting 中将计算机添加到受信任主机列表](https://go.microsoft.com/fwlink/p/?LinkID=135188)。

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

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行。

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
指定具有执行此操作所需访问权限的用户账户。如果未添加该参数或未指定任何值，则该参数的默认值为当前用户。请以以下格式之一输入用户名：

--用户名-- 域名用户-- User@Domain.com-- 由 Get-Credential cmdlet 返回的凭据对象。

如果用户输入了用户名，那么系统会显示一个要求输入密码的提示。

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

### -IncludeManagementTools
该 cmdlet 会卸载所有适用的管理工具，以及由 *Name* 参数指定的角色、角色服务或功能。默认情况下，运行 **Uninstall-WindowsFeature** cmdlet 时不会卸载管理工具；必须添加此参数才能卸载相关的管理工具。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LogPath
指定日志文件的名称和路径。如果此 cmdlet 的结果需要存储在日志文件中，请添加此参数。

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
指定此 cmdlet 将卸载的一系列功能/特性。该参数不支持通配符。

```yaml
Type: Feature[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Remove
该命令表示会从位于 `%SystemDrive%:\Windows\WinSxS` 的并排存储（side-by-side storage）中删除指定 `rrsandfplural` 类型的功能文件。如果该功能尚未被卸载，此命令将会将其卸载。

当你删除功能文件时，依赖于这些文件的各个功能也会被一并删除。如果你删除了某个子功能所对应的功能文件，并且该父功能没有其他子功能被安装的话，那么整个父功能或相关角色的所有文件都会被删除。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Restart
表示如果指定的角色或功能的卸载过程需要重启目标计算机，此cmdlet会自动执行重启操作。此参数不能与*Vhd*参数同时使用。

```yaml
Type: SwitchParameter
Parameter Sets: RunningComputer
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Vhd
指定离线VHD文件的路径。该路径可以指向VHD文件本身，也可以指向通过“部署映像服务与管理”（Deployment Image Servicing and Management，简称DISM）工具已挂载VHD的位置。

VHD可以存储在目标计算机的本地磁盘上，也可以存储在网络共享文件夹中。如果VHD位于网络共享文件夹中，则该参数的值应为指向该VHD的UNC路径（Universal Naming Convention路径）。在这种情况下，用于挂载VHD的计算机的账户必须具有对该共享文件夹的读写权限（在“文件共享”对话框中选择“读取/写入”权限，或在“文件夹属性”对话框的“安全”选项卡上选择“完全控制”权限）；否则将无法访问该VHD。本地回环（Local Loopback）UNC路径是不被支持的。计算机账户可以使用以下两种格式之一：DOMAIN\SERVERNAME$ 或 SERVERNAME$。

使用 *ComputerName* 参数来指定用于挂载 VHD 的目标计算机。如果未指定 *ComputerName* 参数，则会使用本地计算机。用于挂载 VHD 的计算机必须运行 Windows Server 2012 R2 操作系统。通过此参数指定的任何本地路径（例如 D:\myFolder）始终都是相对于目标计算机的。

```yaml
Type: String
Parameter Sets: VhdPath
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.Windows.ServerManager Commands.Feature[]

## 输出

### Microsoft.Windows.ServerManagercommands.FeatureOperationResult

## 备注

## 相关链接

[Get-WindowsFeature](./Get-WindowsFeature.md)

[Install-WindowsFeature](./Install-WindowsFeature.md)

[Enable-ServerManagerStandardUserRemoting](./Enable-ServerManagerStandardUserRemoting.md)

[禁用 ServerManagerStandardUserRemoting 功能](./ Disable-ServerManagerStandardUserRemoting.md)

