---
description: 使用此主题来帮助您使用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmQuotaTemplate.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmquotatemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmQuotaTemplate
---

# New-FsrmQuotaTemplate

## 摘要
创建一个配额模板。

## 语法

```
New-FsrmQuotaTemplate [-Name] <String> [-Description <String>] -Size <UInt64> [-SoftLimit]
 [-Threshold <CimInstance[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmQuotaTemplate` cmdlet 用于创建一个配额模板。配额模板定义了存储空间的使用限制、配额的类型（硬性配额或软性配额），以及（可选的）一组通知机制：当配额使用量达到您设定的阈值时，服务器会自动触发这些通知。

## 示例

### 示例 1：创建一个硬性配额模板
```
PS C:\> New-FsrmQuotaTemplate -Name "1GB limit" -Description "limit usage to 1 GB." -Size 1GB
```

此命令创建了一个名为“1GB limit”的配额模板。该命令为配额模板添加了描述，并配置了一个固定大小限制（1GB），且该限制不设置任何阈值。具有固定大小限制的配额会阻止用户在达到存储空间上限后继续保存文件；当数据量达到各个预设阈值时，系统会生成相应的通知。

### 示例 2：创建一个用于运行命令的软限制配额模板
```
The first command creates an FSRM action object and stores the results in the $Action variable. The action indicates that when an associated event occurs, the server run Cmd.exe with the specified parameters. The command specifies that server record errors codes from the executed command in the error log.
PS C:\> $Action = New-FsrmAction -Type Command -Command "c:\windows\system32\cmd.exe" -CommandParameters "echo [source file path] >> c:\log.txt" -ShouldLogError

The second command creates a threshold object and stores the results in the $Threshold variable. The command specifies the percentage of the quota limit at which to execute the action, and specifies the action stored in the $Action variable.
PS C:\> $Threshold = New-FsrmQuotaThreshold -Percentage 90 -Action $action

The third command creates a quota template named "128MB limit" and specifies the threshold stored in the $Threshold variable. The *SoftLimit* parameter indicates the quota reports on the disk usage with respect to the size limit and run thresholds, but does not enforce the size limit.
PS C:\> New-FsrmQuotaTemplate -Name "128MB limit" -Size 128MB -Threshold $Threshold -SoftLimit
```

这个示例创建了一个配额模板，该模板的软限制为 128MB，使用率达到 90% 时会触发某个阈值，并且会执行一个自定义命令。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，随后再显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

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

### -Description
为配额指定一个描述性说明。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Name
为配额指定一个名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Size
指定了配额所遵循的大小限制。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SoftLimit
这表示配额报告会显示磁盘使用情况与大小限制及运行阈值的对比情况，但并不会强制实施该大小限制。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Threshold
指定一个阈值对象的数组。

`Threshold` 对象定义了在文件操作过程中可以使用到的空间占可用空间的百分比，以及当配额达到该阈值时服务器会执行的一系列操作。要使系统在配额被超出时能够自动执行相应的操作，请将阈值设置为 100（即 100%）。你可以使用 `New-FsrmQuotaThreshold` cmdlet 来创建一个 `Threshold` 对象。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的最大操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或整个计算机。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt64

### System.Management.Automation.SwitchParameter

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmQuotaTemplate](./Get-FsrmQuotaTemplate.md)

[Remove-FsrmQuotaTemplate](./Remove-FsrmQuotaTemplate.md)

[Set-FsrmQuotaTemplate](./Set-FsrmQuotaTemplate.md)

