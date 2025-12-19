---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/get-windowsfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-WindowsFeature
---

# Get-WindowsFeature

## 摘要
获取有关指定服务器上可安装和已安装的 Windows Server 角色、角色服务以及功能的信息。

## 语法

```
Get-WindowsFeature [[-Name] <String[]>] [-Vhd <String>] [-ComputerName <String>] [-Credential <PSCredential>]
 [-LogPath <String>] [<CommonParameters>]
```

## 描述
`Get-WindowsFeature` cmdlet 可以获取有关可在计算机上安装的功能以及已安装在运行 Windows Server 2012 R2 的计算机上的功能的信息。该计算机可以是物理设备，也可以是运行 Windows Server 2012 R2 的离线虚拟硬盘（VHD）。

## 示例

### 示例 1：获取指定计算机上可用且已安装的功能列表
```
PS C:\> Get-WindowsFeature -ComputerName "Server1" -Credential "contoso.com\user1"
```

该命令用于获取目标计算机（名为Server1）上可用且已安装的功能列表。提供了Contoso.com域中用户user1的凭据，该用户在Server1上具有管理员权限。

### 示例 2：获取指定离线 VHD 上可用且已安装的功能列表
```
PS C:\> Get-WindowsFeature -Vhd "D:\ps-test\vhd1.vhd"
```

此命令会获取位于 D:\ps-test\vhd1.vhd 的指定离线 VHD 上可用且已安装的功能列表。

### 示例 3：通过命令 ID 获取可用和已安装的功能列表
```
PS C:\> Get-WindowsFeature -Name "AD*, Web*"
```

这个命令会获取所有可用和已安装的功能列表，这些功能的命令ID以“AD”或“Web”开头。

### 示例 4：获取特定服务器上已安装的功能列表
```
PS C:\> Get-WindowsFeature -ComputerName "Server01" | Where Installed
```

此命令会获取名为Server01的服务器上安装的所有功能的列表。

### 示例 5：获取服务器上具有已删除安装文件的特性列表
```
PS C:\> Get-WindowsFeature -ComputerName "Server01" | Where InstallState -Eq Removed
```

这个命令会获取服务器 Server01 上的所有特性列表。这些特性的安装文件已经从本地的并行存储系统中被删除，因此需要通过外部文件源来进行安装。

## 参数

### -ComputerName
指定从运行 Windows Server 2012 R2 的远程计算机上可用的 rrsandf_plural 列表。该参数仅接受一个计算机名称。如果未添加此参数或未指定任何计算机名称，则默认目标为本地计算机。该参数的有效值包括远程计算机的 NetBIOS 名称、IP 地址或完全限定域名（FQDN）。

要使用远程计算机的 IP 地址作为此参数的值，您的命令必须包含 *Credential* 参数。该计算机必须配置为支持 HTTPS 传输，或者远程计算机的 IP 地址必须被添加到本地计算机的 WinRM TrustedHosts 列表中。有关如何将计算机名称添加到 WinRM TrustedHosts 列表中的信息，请参阅 [如何在 about_Remote_Troubleshooting 中将计算机添加到受信任主机列表](https://go.microsoft.com/fwlink/p/?LinkID=135188)。

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

### -Credential
指定一个具有执行此操作所需访问权限的用户账户。如果未添加该参数或未指定任何值，该参数的默认值为当前用户。请以以下格式之一输入用户名（引号是可选的）。

-- "用户名" -- "域名\用户" -- "User@Domain.com" -- 由 [Get-Credential](https://go.microsoft.com/fwlink/p/?LinkID=113311) 命令返回的凭据对象。

如果输入了用户名，系统会显示一个要求输入密码的提示框。

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

### -LogPath
指定日志文件的名称和路径。如果需要将此 cmdlet 的结果存储在日志文件中，请使用此参数。

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
指定一个命令ID数组，这些ID对应于角色、角色服务或功能。该Cmdlet将从这些角色/服务/功能中返回相关信息。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Vhd
指定离线虚拟硬盘（VHD）的路径。该路径可以指向一个VHD文件，也可以指向一个已通过部署映像服务和管理（DISM）工具挂载了VHD的位置。

VHD可以位于目标计算机上的本地磁盘上，也可以位于网络共享文件夹中。如果VHD位于网络共享文件夹中，则该参数的值为指向该VHD的UNC路径。在这种情况下，用于挂载VHD的计算机的账户必须具有对该共享文件夹的读写权限（在“文件共享”对话框中选择“读/写”权限，或在“文件夹属性”对话框的“安全”选项卡中选择“完全控制”权限），否则将无法访问该VHD。本地回环UNC路径是不被支持的。计算机账户可以使用以下两种格式之一：DOMAIN\SERVERNAME$ 或 SERVERNAME$.

请添加 *ComputerName* 参数，以指定用于挂载 VHD 的目标计算机。如果未指定 *ComputerName* 参数，则会使用本地计算机。用于挂载 VHD 的计算机必须运行 Windows Server 2012 R2 操作系统。通过此参数指定的任何本地路径（例如 D:\myFolder）始终是相对于目标计算机的。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

## 输出

### Microsoft.Windows.ServerManager Commands.Feature[]

## 备注

## 相关链接

[Install-WindowsFeature](./Install-WindowsFeature.md)

[Uninstall-WindowsFeature](./Uninstall-WindowsFeature.md)

[Enable-ServerManagerStandardUserRemoting](./Enable-ServerManagerStandardUserRemoting.md)

[禁用 ServerManager 标准用户远程访问功能](./ Disable-ServerManagerStandardUserRemoting.md)

