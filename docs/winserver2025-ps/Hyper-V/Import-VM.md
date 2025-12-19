---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/import-vm?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-VM
---

# 导入虚拟机

## 摘要
从文件中导入一个虚拟机。

## 语法

### 注册（默认选项）
```
Import-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Path] <String> [-Register] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 复制
```
Import-VM [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Path] <String> [[-VhdDestinationPath] <String>] [-Copy] [-VirtualMachinePath <String>]
 [-SnapshotFilePath <String>] [-SmartPagingFilePath <String>] [-VhdSourcePath <String>] [-GenerateNewId]
 [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 兼容性报告
```
Import-VM [-CompatibilityReport] <VMCompatibilityReport> [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Import-VM` cmdlet 用于从文件中导入虚拟机。

## 示例

### 示例 1
```
PS C:\> Import-VM -Path 'C:\<vm export path>\2B91FEB3-F1E0-4FFF-B8BE-29CED892A95A.vmcx'
```

从配置文件中导入虚拟机。该虚拟机会被直接注册到系统中，因此其文件不会被复制。

### 示例 2
```
PS C:\> Import-VM -Path 'C:\<vm export path>\2B91FEB3-F1E0-4FFF-B8BE-29CED892A95A.vmcx' -Copy -GenerateNewId
```

通过将虚拟机的文件复制到Hyper-V主机的默认虚拟机存储位置和虚拟硬盘存储位置来导入该虚拟机。导入后的虚拟机会被赋予一个新的唯一标识符（而不是配置文件中的那个标识符）。当您需要导入多个虚拟机副本时，这种方法非常有用，因为每个虚拟机都必须具有唯一的标识符。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: Register, Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CompatibilityReport
指定一份兼容性报告，该报告用于解决虚拟机与Hyper-V主机之间的任何不兼容问题。

```yaml
Type: VMCompatibilityReport
Parameter Sets: CompatibilityReport
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于导入虚拟机的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址或完全限定域名作为主机标识。默认值是本地计算机。可以使用 “localhost” 或句点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Register, Copy
Aliases:

Required: False
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

### -Copy
指定将导入的虚拟机的文件复制到服务器的默认位置，而不是直接在原地注册该虚拟机。

```yaml
Type: SwitchParameter
Parameter Sets: Copy
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Register, Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GenerateNewId
指定导入的虚拟机应被复制，并赋予一个新的唯一标识符。（默认情况下，**Import-VM** 会为新的虚拟机分配与被导入的虚拟机相同的唯一标识符。）

```yaml
Type: SwitchParameter
Parameter Sets: Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定要导入的导出虚拟机的路径。

```yaml
Type: String
Parameter Sets: Register, Copy
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Register
指定导入的虚拟机将直接在当前位置进行注册，而不是将其文件复制到服务器的默认存储路径中。如果虚拟机的文件已经位于其需要运行的位置，请选择此选项。

```yaml
Type: SwitchParameter
Parameter Sets: Register
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SmartPagingFilePath
指定用于智能分页文件的新路径（如果需要的话）。

```yaml
Type: String
Parameter Sets: Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SnapshotFilePath
指定与虚拟机相关的任何快照文件的路径。

```yaml
Type: String
Parameter Sets: Copy
Aliases: CheckpointFileLocation, SnapshotFileLocation

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VhdDestinationPath
指定用于复制虚拟机VHD文件的文件夹。

```yaml
Type: String
Parameter Sets: Copy
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VhdSourcePath
指定用于复制虚拟机VHD文件的文件夹。

```yaml
Type: String
Parameter Sets: Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VirtualMachinePath
指定用于存储虚拟机配置文件的路径。

```yaml
Type: String
Parameter Sets: Copy
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### 无

## 输出

### Microsoft.HyperV.PowerShell.VirtualMachine

## 备注

## 相关链接

