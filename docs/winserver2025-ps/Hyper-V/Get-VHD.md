---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VHD
---

# Get-VHD

## 摘要
获取与虚拟硬盘相关的信息。

## 语法

### 路径（默认值）
```
Get-VHD [-Path] <String[]> [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

### 磁盘
```
Get-VHD [-DiskNumber] <UInt32> [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

### VMId
```
Get-VHD [-VMId] <Guid[]> [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [<CommonParameters>]
```

## 描述
`Get-VHD` cmdlet 可以获取与虚拟硬盘相关联的虚拟硬盘对象。

> [!注意] > 当 VHD 正在被使用中（例如被虚拟机占用或在操作系统中挂载），并且它位于共享存储空间上时，`Get-VHD` 命令只能从正在使用它的主机上访问该 VHD。任何其他尝试运行 `Get-VHD` 命令的服务器都会收到错误提示，表示该 VHD 正在被使用中。

## 示例

### 示例 1
```powershell
PS C:\> Get-VHD -Path C:\test\testvhdx.vhdx
```

获取该虚拟硬盘文件所在的虚拟硬盘位置，其路径为 `C:\test\testvhdx.vhdx`。

### 示例 2
```powershell
PS C:\> Get-VHD -DiskNumber 6
```

将虚拟硬盘连接到系统中，并为其分配盘号6。

### 示例 3
```powershell
PS C:\> Get-VM -VMName TestVM | Select-Object -Property VMId | Get-VHD
```

使用管道功能（pipeline feature）和参数 VMId，获取与虚拟机 TestVM 相关联的虚拟硬盘对象。

### 示例 4
```powershell
PS C:\> Get-VM -VMName TestVM | Select-Object -Property VMId | Get-VHD
```

使用管道功能（pipeline feature）和路径参数（path parameter），获取与虚拟机TestVM相关联的虚拟硬盘对象。

### 示例 5
```powershell
PS C:\> Get-ChildItem -Path C:\test -Recurse -Include *.vhd, *.vhdx, *.vhds, *.avhd, *.avhdx | Get-VHD
```

获取指定目录及其子目录中包含的所有虚拟硬盘文件对应的虚拟硬盘对象。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于检索虚拟硬盘的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全qualified 的域名进行指定。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DiskNumber
指定要与要检索的虚拟硬盘相关联的磁盘编号。

```yaml
Type: UInt32
Parameter Sets: Disk
Aliases: Number

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定要检索的虚拟硬盘的虚拟硬盘文件的路径。如果指定了文件名或相对路径，则该路径会相对于当前工作目录进行计算。

```yaml
Type: String[]
Parameter Sets: Path
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -VMId
指定要获取其虚拟硬盘的虚拟机的标识符。

```yaml
Type: Guid[]
Parameter Sets: VMId
Aliases: Id

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Vhd.PowerShell.VirtualHardDisk

## 备注

## 相关链接

