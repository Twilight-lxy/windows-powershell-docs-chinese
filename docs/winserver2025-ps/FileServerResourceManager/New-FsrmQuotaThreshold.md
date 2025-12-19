---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMQuotaThreshold.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmquotathreshold?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmQuotaThreshold
---

# New-FsrmQuotaThreshold

## 摘要
返回一个配额阈值对象。

## 语法

```
New-FsrmQuotaThreshold [-Percentage] <UInt32> [-Action <CimInstance[]>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmQuotaThreshold` cmdlet 返回一个阈值对象。您可以使用该阈值对象来创建文件服务器资源管理器（FSRM）的配额和配额模板。

## 示例

### 示例 1：设置配额阈值
```
PS C:\> $Action = New-FsrmAction -Type Command -Command "c:\windows\system32\cmd.exe" -CommandParameters "echo [source file path] >> c:\log.txt" -ShouldLogError
PS C:\> New-FsrmQuotaThreshold -Percentage 90 -Action $Action
```

第一个命令创建了一个FSRM（File System Reporting Manager）操作对象，并将结果存储在$Action变量中。该操作表明：当相关事件发生时，服务器会运行Cmd.exe并使用指定的参数。同时，该命令还要求服务器将命令执行过程中产生的错误代码记录到错误日志中。

第二个命令返回一个阈值对象。该命令规定：当使用量达到配额限制的90%时，服务器会执行存储在$Action变量中的相应操作。

## 参数

### -Action
指定一个FSRM（Fault Service Repair Manager）操作数组。您可以使用**New-FsrmAction** cmdlet来创建一个新的操作。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，随后会显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

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

### -Percentage
指定在达到配额限制的多少百分比时执行该操作。可以设置的最大值为 259。

```yaml
Type: UInt32
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

## 备注

## 相关链接

[New-FsrmAction](./New-FsrmAction.md)

[New-FsrmQuota](./New-FsrmQuota.md)

[New-FsrmQuotaTemplate](./New-FsrmQuotaTemplate.md)

[Set-FsrmQuota](./Set-FsrmQuota.md)

[Set-FsrmQuotaTemplate](./Set-FsrmQuotaTemplate.md)

