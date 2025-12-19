---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMAutoQuota.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/set-fsrmautoquota?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-FsrmAutoQuota
---

# Set-FsrmAutoQuota

## 摘要
更改自动应用配额的配置设置。

## 语法

### 查询（cdxml）（默认值）
```
Set-FsrmAutoQuota [-Path] <String> [-Template <String>] [-Disabled] [-UpdateDerived] [-UpdateDerivedMatching]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### InputObject (cdxml)
```
Set-FsrmAutoQuota -InputObject <CimInstance[]> [-Template <String>] [-Disabled] [-UpdateDerived]
 [-UpdateDerivedMatching] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-FsrmAutoQuota` cmdlet 用于更改自动应用配额的配置设置。如果您希望保留现有的配额不变，但让修改后的自动应用配额对新子文件夹生效，请不要指定 `UpdateDerived` 或 `UpdateDerivedMatching` 参数。

当你对自动应用配额进行修改时，可以选择将这些修改扩展到该自动应用配额路径下的所有现有配额。你可以指定 `UpdateDerivedMatching` 参数，仅修改那些仍与原始自动应用配额匹配的配额；或者你也可以指定 `UpdateDerived` 参数，来修改该自动应用配额路径下的所有配额——无论自创建这些配额以来你对它们做了哪些更改。

## 示例

#### 示例 1：为自动配额功能设置模板
```
PS C:\> Set-FsrmAutoQuota -Path "C:\Shares\CtrShare01" -Template "200 MB Limit Reports to User"
```

此命令将名为“200 MB Limit Reports to User”的模板设置为自动应用配额的模板，用于C:\Shares\CtrShare01文件夹。

### 示例 2：为所有配额设置模板
```
PS C:\> Set-FsrmAutoQuota -Path "C:\Shares\CtrShare01" -Template "200 MB Limit Reports to User" -UpdateDerived
```

此命令将为名为“C:\Shares\CtrShare01”的自动应用配额路径中的所有现有配额，设置一个名为“200 MB Limit Reports to User”的模板。

### 示例 3：为未修改的配额设置模板
```
PS C:\> Set-FsrmAutoQuota -Path "C:\Shares\CtrShare01" -Template "200 MB Limit Reports to User" -UpdateDerivedMatching
```

此命令将名为“200 MB Limit Reports to User”的模板应用于仅位于自动配额路径“C:\ Shares\CtrShare01”中的那些配额。这些配额自被自动生成以来未被修改过。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用 `*-Job` cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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
在运行 cmdlet 之前会提示您进行确认。

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

### -Disabled
表示自动配额功能处于禁用状态。服务器不会跟踪该配额的使用数据，也不会执行任何与配额阈值相关的操作。

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

### -InputObject
指定要传递给此cmdlet的输入数据。您可以使用该参数，也可以将输入数据通过管道（pipe）传递给此cmdlet。

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

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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
指定一个有效的本地文件夹路径。

```yaml
Type: String
Parameter Sets: Query (cdxml)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Template
在服务器上指定一个配额模板的名称。

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

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
表示服务器会修改自动应用配额路径中所有现有的配额设置。

如果您指定了此参数，则无法指定*UpdateDerivedMatching*参数。

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
表示服务器仅更新自自动生成以来未被修改过的配额。如果您有某些配额在自动生成后被修改过，但不希望再对这些配额进行任何更改，请指定此参数。

如果您指定了这个参数，则无法指定 *UpdateDerived* 参数。

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
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被执行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMAutoQuota

## 备注

## 相关链接

[Get-FsrmAutoQuota](./Get-FsrmAutoQuota.md)

[New-FsrmAutoQuota](./New-FsrmAutoQuota.md)

[Remove-FsrmAutoQuota](./Remove-FsrmAutoQuota.md)

[更新-FsrmAutoQuota](./Update-FsrmAutoQuota.md)

