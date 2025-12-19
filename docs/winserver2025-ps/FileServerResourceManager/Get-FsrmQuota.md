---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmQuota.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/get-fsrmquota?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-FsrmQuota
---

# Get-FsrmQuota

## 摘要
在服务器上获取FSRM（文件系统资源管理）配额。

## 语法

```
Get-FsrmQuota [[-Path] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-FsrmQuota` cmdlet 可以获取服务器上的一个或多个文件服务器资源管理器（FSRM）配额信息。

## 示例

### 示例 1：获取所有配额
```
PS C:\> Get-FsrmQuota
```

这个命令可以获取服务器上的所有配额信息。

### 示例 2：通过使用路径来获取配额
```
PS C:\> Get-FsrmQuota -Path "C:\Share01\..."
```

这个命令会获取 C:\Share01 目录下的所有配额信息，以及 C:\Share01 所有子文件夹中的所有配额信息。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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

### -Path
指定包含配额信息的本地文件夹。

此参数支持递归路径和通配符路径。要指定一个递归路径，需要在路径中添加“\...”。例如，C:\Share01\... 表示 C:\Share01 中的所有配额以及 C:\Share01 的所有子文件夹中的所有配额。要在路径中使用通配符，可以在路径中添加星号（*）和问号（?）。例如，C:\Share01\*A 表示 C:\Share01 中的所有配额以及 C:\Share01 的子文件夹中名称以字母 A 开头的所有配额。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMQuota

## 备注

## 相关链接

[New-FsrmQuota](./New-FsrmQuota.md)

[Remove-FsrmQuota](./Remove-FsrmQuota.md)

[Reset-FsrmQuota](./Reset-FsrmQuota.md)

[Set-FsrmQuota](./Set-FsrmQuota.md)

[更新-FsrmQuota](./Update-FsrmQuota.md)

