---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BranchCacheOrchestrator.cdxml-help.xml
Module Name: BranchCache
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/branchcache/export-bccachepackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-BCCachePackage
---

# Export-BCCachePackage

## 摘要
导出一个缓存包。

## 语法

### StagingPath（默认值）
```
Export-BCCachePackage -Destination <String> [-Force] [[-StagingPath] <String>] [-OutputReferenceFile <String>]
 [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ExportDataCache
```
Export-BCCachePackage -Destination <String> [-Force] [-ExportDataCache] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Export-BCCachePackage` cmdlet 用于导出缓存包。

## 示例

#### 示例 1：导出内容
```
PS C:\> Export-BCDataPackage -Destination "D:\temp"
```

此命令使用 **Publish-BCFileContent** 和 **Publish-BCWebContent** cmdlet 将所有已被哈希处理的内容导出。该命令将包含这些数据的包导出到 D:\temp 目录中。

## 参数

### -AsJob
以后台作业的形式运行该 cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，则可以使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。输入计算机名称或会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值为本地计算机上的当前会话。

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

### -Destination
指定数据包存储的文件夹位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExportDataCache
指定将本地数据缓存的内容包含在包中。

```yaml
Type: SwitchParameter
Parameter Sets: ExportDataCache
Aliases:

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

### -OutputReferenceFile
指定用于生成输出参考文件的文件夹位置。

```yaml
Type: String
Parameter Sets: StagingPath
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StagingPath
指定此cmdlet所打包的缓存文件的文件夹位置。这些文件是由**Publish-BCFileContent** cmdlet生成的。

```yaml
Type: String
Parameter Sets: StagingPath
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[Import-BCCachePackage](./Import-BCCachePackage.md)

[Publish-BCFileContent](./Publish-BCFileContent.md)

[发布-BCWeb内容](./Publish-BCWebContent.md)

