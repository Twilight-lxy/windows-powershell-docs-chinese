---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.Modernizer.Cmdlets.dll-Help.xml
Module Name: AppvSequencer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvsequencer/expand-appvsequencerpackage?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Expand-AppvSequencerPackage
---

# Expand-AppvSequencerPackage

## 摘要
用于扩展现有的 App-V 包。

## 语法

```
Expand-AppvSequencerPackage [-AppvPackagePath] <String> [<CommonParameters>]
```

## 描述
`Expand-AppvSequencerPackage` cmdlet 将 Microsoft 应用程序虚拟化（App-V）包扩展为其在运行序列器的计算机上的 NTFS 文件系统中的原始格式。这样，在生成包之前，您可以更轻松地向序列器中添加先决条件或依赖应用程序。

每次运行此cmdlet时，都可以将一个新的软件包安装到正在运行sequencer的计算机上。

## 示例

#### 示例 1：扩展一个包
```
PS C:\> Expand-AppvSequencerPackage -AppvPackagePath "C:\MyPackages\PreReq.appv"
```

这个命令将PreReq.appv包扩展到测序计算机上。

## 参数

### -AppvPackagePath
指定一个现有的 App-V 包的文件路径，该包将被扩展到运行该 cmdlet 的计算机的 NTFS 文件系统中。

```yaml
Type: String
Parameter Sets: (All)
Aliases: AppvPackage

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[New-AppvSequencerPackage](./New-AppvSequencerPackage.md)

[更新 AppvSequencerPackage](./Update-AppvSequencerPackage.md)

