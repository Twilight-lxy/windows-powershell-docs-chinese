---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/copy-vmfile?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Copy-VMFile
---

# 复制虚拟机文件

## 摘要
将文件复制到虚拟机中。

## 语法

### 名称（默认值）
```
Copy-VMFile [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-SourcePath] <String> [-DestinationPath] <String> -FileSource <CopyFileSourceType>
 [-CreateFullPath] [-Force] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Copy-VMFile [-VM] <VirtualMachine[]> [-SourcePath] <String> [-DestinationPath] <String>
 -FileSource <CopyFileSourceType> [-CreateFullPath] [-Force] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Copy-VMFile` cmdlet 将一个文件复制到虚拟机中。

## 示例

### 示例 1
```
PS C:\> Copy-VMFile "Test VM" -SourcePath "D:\Test.txt" -DestinationPath "C:\Temp\Test.txt" -CreateFullPath -FileSource Host
```

这个示例将文件“test.txt”从主机操作系统复制到虚拟机“Test VM”的客户机操作系统中。如果“C:\Temp”目录尚不存在，系统会自动创建该目录。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个Hyper-V主机的数组。此cmdlet会将文件复制到您指定的这些主机上。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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

### -CreateFullPath
这表示当该cmdlet复制文件时，如果目标文件夹尚不存在，它会创建相应的文件夹。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationPath
指定一个路径。该cmdlet会将文件复制到目标路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FileSource
用于指定文件源的类型。

```yaml
Type: CopyFileSourceType
Parameter Sets: (All)
Aliases:
Accepted values: Host

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需请求用户确认。

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

### -Name
按名称指定一组虚拟机对象数组。此cmdlet会将文件复制到您指定的虚拟机上。

```yaml
Type: String[]
Parameter Sets: Name
Aliases: VMName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SourcePath
用于指定路径。该cmdlet会从源路径复制文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VM
指定一个虚拟机对象的数组。该cmdlet会将文件复制到您指定的虚拟机上。要获取虚拟机对象，请使用**Get-VM** cmdlet。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上该cmdlet并没有被运行。

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

## 输出

## 备注

## 相关链接

