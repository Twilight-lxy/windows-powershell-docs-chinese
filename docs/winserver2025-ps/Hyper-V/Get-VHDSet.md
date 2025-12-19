---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vhdset?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VHDSet
---

# Get-VHDSet

## 摘要
获取有关VHD集的信息。

## 语法

```
Get-VHDSet [-Path] <String[]> [-GetAllPaths] [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述
`Get-VHDSet` cmdlet 可以获取有关虚拟硬盘（VHD）集文件的信息。这些信息包括该集合中包含的所有检查点的列表。

“Checkpoint”取代了之前的术语“snapshot”。

## 示例

### 示例 1：获取一个 VHD 集合及其依赖的文件
```
PS C:\> Get-VHDSet -Path "Data01.vhds" -GetAllPaths
```

这个命令用于获取关于VHD集合文件Data01.vhds的信息。这些信息包括该VHD集合所依赖的所有文件的路径。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全合格的域名进行识别。默认值是本地计算机。可以使用“localhost”或点（.）来明确指出本地计算机。

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

### -GetAllPaths
表示此cmdlet会获取所有依赖该VHD集合文件的文件的路径。

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

### -Path
指定一个包含 VHD 配置文件路径的数组，该cmdlet将从这些路径中获取所需的数据。如果您仅提供了一个文件名或相对路径，cmdlet 会自动计算出相对于当前工作文件夹的完整路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Vhd.PowerShell.VHDSetInfo
此cmdlet返回**VHDSetInfo**对象。

## 备注

## 相关链接

[Optimize-VHDSet](./Optimize-VHDSet.md)

