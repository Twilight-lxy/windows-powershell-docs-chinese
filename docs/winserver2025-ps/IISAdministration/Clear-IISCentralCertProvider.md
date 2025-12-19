---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/clear-iiscentralcertprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-IISCentralCertProvider
---

# 清除 IISCentralCertProvider

## 摘要
从 IIS 的中央证书存储中删除配置信息。

## 语法

```
Clear-IISCentralCertProvider [-Force] [<CommonParameters>]
```

## 描述
`Clear-IISCentralCertProvider` cmdlet 会删除与中央证书提供者相关的所有设置。如果启用了“中央证书存储”功能，必须指定 `Force` 参数。一旦指定了 `Force`，该功能将被禁用，并且所有相关设置都会被清除。如果“中央证书存储”功能已经被禁用，则无需再指定 `Force` 参数。

## 示例

### 示例 1：从 IIS 证书存储中清除配置信息
```
PS C:\> Clear-IISCentralCertProvider
```

此命令会删除 IIS 中央证书存储的所有配置信息，但不会删除该证书存储提供者本身。

## 参数

### -Force
强制命令执行，而无需请求用户确认。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[禁用 IISCentralCertProvider](./ Disable-IISCentralCertProvider.md)

[Enable-IISCentralCertProvider](./Enable-IISCentralCertProvider.md)

[Get-IISCentralCertProvider](./Get-IISCentralCertProvider.md)

[Set-IISCentralCertProvider](./Set-IISCentralCertProvider.md)

[设置 IISCentralCertProviderCredential](./Set-IISCentralCertProviderCredential.md)

