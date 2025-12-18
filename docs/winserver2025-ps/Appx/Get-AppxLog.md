---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.Appx.PackageManager.Commands.dll-help.xml
Module Name: Appx
ms.date: 05/15/2023
online version: https://learn.microsoft.com/powershell/module/appx/get-appxlog?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AppxLog
---

# 获取 AppX 日志

## 摘要
获取应用程序包安装日志。

## 语法

### 全部（默认设置）

```
Get-AppxLog [-All] [<CommonParameters>]
```

### ActivityId

```
Get-AppxLog [-ActivityId <System.String>] [<CommonParameters>]
```

## 描述

`Get-AppxLog` cmdlet 可以获取在应用程序包部署过程中生成的安装日志。应用程序包的文件扩展名为 `.msix` 或 `.appx`。该日志包含了错误信息、警告提示，以及有关 Appx Windows PowerShell 模块中使用的 cmdlets 启动的进程的其他详细信息。

当 `Add-AppxPackage` 或 `Remove-AppxPackage` 命令执行失败时，它们会返回一个 **ActivityID**，该 ID 可以与 `Get-AppxLog` 命令一起使用。

有关常见错误代码的更多信息，请参阅[故障排除：Windows应用商店应用的打包、部署和查询](https://go.microsoft.com/fwlink/?LinkId=271201)。

## 示例

#### 示例 1：获取最近一次部署的日志

```powershell
Get-AppxLog
```

这个命令可以获取与最近一次部署操作相关的日志信息。

### 示例 2：获取所有日志的详细信息

```powershell
Get-AppxLog -All
```

这个命令可以获取计算机上所有应用程序包安装日志。

## 参数

### -ActivityId

指定一个活动ID。此cmdlet使用该ID来获取特定应用程序包安装的日志信息。

```yaml
Type: System.String
Parameter Sets: ActivityId
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -All

表示该cmdlet会获取计算机上的所有日志。当您以管理员身份在Windows PowerShell中运行此cmdlet时，可以获取更多相关信息。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: All
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.System.String[]

## 输出

```csharp
### System.Diagnostics.Eventing.Reader.EventLogRecord
```

## 备注

## 相关链接

[包管理器 API](https://go.microsoft.com/fwlink/?LinkId=245447)

[如何添加和删除应用程序](https://go.microsoft.com/fwlink/?LinkID=231020)

[解决Windows应用商店应用的打包、部署和查询相关问题](https://go.microsoft.com/fwlink/?LinkId=271201)

[Get-AppxPackage](./Get-AppxPackage.md)

[Get-AppxPackageManifest](./Get-AppxPackageManifest.md)

[Get-AppxLastError](./Get-AppxLastError.md)
