---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FSRMAutoQuota.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/get-fsrmautoquota?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-FsrmAutoQuota
---

# Get-FsrmAutoQuota

## 摘要
在服务器上自动应用配额设置。

## 语法

```
Get-FsrmAutoQuota [[-Path] <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [<CommonParameters>]
```

## 描述
`Get-FsrmAutoQuota` cmdlet 可以获取某个卷或文件夹上的自动应用配额（auto apply quota）信息。自动应用配额是一种配额模板，您可以将这种模板分配给父级卷或文件夹。

## 示例

### 示例 1：获取所有自动应用的配额
```
PS C:\> Get-FsrmAutoQuota
```

这个命令可以获取本地服务器上所有自动应用的配额信息。

### 示例 2：通过使用路径来获取自动应用的配额
```
PS C:\> Get-FsrmAutoQuota -Path "C:\Share01\..."
```

这个命令会获取 C:\Share01 中所有的自动应用配额，以及 C:\Share01 所有子文件夹中的所有自动应用配额。

## 参数

### -AsJob
将 cmdlet 作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个有效的本地文件夹路径。

此参数支持递归路径和通配符路径。要指定一个递归路径，需要在路径后面添加 “\…”。例如，C:\Share01\… 表示 C:\Share1 中的所有自动应用配额，以及 C:\Share01 的所有子文件夹中的所有自动应用配额。

要在路径中指定通配符，可以在路径中添加星号（*）和问号（?）。例如，C:\Share01\*A 表示 C:\Share01 中的所有自动应用配额，以及 C:\Share01 的子文件夹中名称以字母 A 开头的所有自动应用配额。

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
该参数用于指定可以同时运行的最大并发操作数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。该限制仅适用于当前执行的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

## 输出

### Microsoft.ManagementInfrastructure.CimInstance

### Microsoft.ManagementInfrastructure.CimInstance#Root/Microsoft/Windows/FSRM/MSFT_FSRMAutoQuota

## 备注

## 相关链接

[New-FsrmAutoQuota](./New-FsrmAutoQuota.md)

[Remove-FsrmAutoQuota](./Remove-FsrmAutoQuota.md)

[Set-FsrmAutoQuota](./Set-FsrmAutoQuota.md)

[更新-FsrmAutoQuota](./Update-FsrmAutoQuota.md)

