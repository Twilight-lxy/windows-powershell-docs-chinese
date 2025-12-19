---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/stop-iiscommitdelay?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-IISCommitDelay
---

# 停止 IIS 提交延迟（Stop-IISCommitDelay）

## 摘要
指示 IIS 配置系统恢复对更改的提交（即让这些更改生效）。

## 语法

```
Stop-IISCommitDelay [[-Commit] <Boolean>] [<CommonParameters>]
```

## 描述
`Stop-IISCommitDelay` cmdlet 命令用于指示 Internet Information Services (IIS) 配置系统恢复对更改的提交（即应用这些更改）。

## 示例

### 示例 1：提交配置更改
```
PS C:\> Stop-IISCommitDelay -Commit $True
```

此命令会提交自从执行 **Start-IISCommitDelay** cmdlet 以来所做的配置更改。

### 示例 2：忽略配置更改
```
PS C:\> Stop-IISCommitDelay -Commit $False
```

此命令会撤销自执行 **Start-IISCommitDelay** cmdlet 以来所做的配置更改。

## 参数

### -Commit
如果值为 `True`，则表示该cmdlet会应用这些更改；否则（如果值为 `False`），则该cmdlet会丢弃这些更改。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.Boolean

## 输出

### System.Object

## 备注

## 相关链接

[Start-IISCommitDelay](./Start-IISCommitDelay.md)

[适用于 Windows PowerShell 的 IIS 管理 cmdlet](./iisadministration.md)

