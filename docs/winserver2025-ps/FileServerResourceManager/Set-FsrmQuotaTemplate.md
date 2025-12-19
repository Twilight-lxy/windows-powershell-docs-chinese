---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmQuotaTemplate.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmquotatemplate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmQuotaTemplate
---

# Set-FsrmQuotaTemplate

## 摘要
更改 FSRM 配额模板的配置设置。

## 语法

### 查询（cdxml）（默认值）
```
Set-FsrmQuotaTemplate [-Name] <String[]> [-Description <String>] [-Size <UInt64>] [-SoftLimit] [-UpdateDerived]
 [-UpdateDerivedMatching] [-Threshold <CimInstance[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-FsrmQuotaTemplate -InputObject <CimInstance[]> [-Description <String>] [-Size <UInt64>] [-SoftLimit]
 [-UpdateDerived] [-UpdateDerivedMatching] [-Threshold <CimInstance[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-FsrmQuotaTemplate` cmdlet 可用于更改一个或多个文件服务器资源管理器（File Server Resource Manager，简称 FSRM）配额模板的配置设置。

当你对某个配额模板进行修改时，可以选择将这些修改应用到所有从该模板派生出来的现有配额上。你可以指定 `UpdateDerivedMatching` 参数，仅修改那些仍然与原始配额模板匹配的配额；或者你可以指定 `UpdateDerived` 参数，修改所有从该模板派生出来的配额，而不管自创建这些配额以来你对它们做了哪些更改。

## 示例

#### 示例 1：修改配额模板中的大小限制
```
PS C:\> Set-FsrmQuotaTemplate -Name "1GB limit" -Description "limit usage to 1.5 GB." -Size 1.5GB
```

这个命令将名为“1GB限制”的配额模板修改为1.5GB的限制，并为该配额模板添加了描述。

### 示例 2：修改所有从配额模板派生的配额的大小限制
```
PS C:\> Set-FsrmQuotaTemplate "1GB limit" -Description "limit usage to 1.5 GB." -Size 1.5GB -UpdateDerived
```

这个命令将名为“1GB限制”的配额模板修改为1.5GB的限制。*UpdateDerived*参数表示，该命令会更新服务器上所有基于该配额模板生成的配额，使其也都设置为1.5GB的限制。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用该参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

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
在运行 cmdlet 之前，会提示您确认是否要执行该操作。

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
Accept pipeline input: False
Accept wildcard characters: False
```

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用这个参数，也可以将输入数据通过管道（pipe）传递给该cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定一个包含配额模板名称的数组。

```yaml
Type: String[]
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Size
指定了配额所遵循的大小限制。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SoftLimit
这表示配额报告会显示磁盘使用情况与大小限制及运行阈值之间的关系，但并不会强制执行该大小限制。

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

### -Threshold
指定一个阈值对象数组。

`Threshold` 对象用于定义在文件操作过程中可以使用空间占可用空间的百分比，以及当配额达到该阈值时服务器应采取的一系列操作。若要使服务器在配额被超出时执行特定操作，可以将阈值设置为 100（即 100%）。您可以使用 `New-FsrmQuotaThreshold` cmdlet 来创建一个 `Threshold` 对象。

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
该参数用于指定可以同时运行的并发操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不影响整个会话或计算机本身。

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

### -UpdateDerived
表示服务器会修改所有从配额模板派生出的配额。如果您指定了此参数，则无法指定 *UpdateDerivedMatching* 参数。

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

### -UpdateDerivedMatching
表示服务器仅更新那些自创建配额以来未被修改的、来自配额模板的配额。如果您有一些在自动生成后被修改过的配额，并且不希望更改它们，请指定此参数。

如果您指定了这个参数，那么就不能指定 *UpdateDerived* 参数了。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未执行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMQuotaTemplate

## 备注

## 相关链接

[Get-FsrmQuotaTemplate](./Get-FsrmQuotaTemplate.md)

[New-FsrmQuotaTemplate](./New-FsrmQuotaTemplate.md)

[New-FsrmQuotaThreshold](./New-FsrmQuotaThreshold.md)

[Remove-FsrmQuotaTemplate](./Remove-FsrmQuotaTemplate.md)

