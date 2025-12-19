---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/disable-iiscentralcertprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-IISCentralCertProvider
---

# 禁用 IISCentralCertProvider

## 摘要
禁用IIS中央证书存储。

## 语法

```
Disable-IISCentralCertProvider [<CommonParameters>]
```

## 描述
`Disable-IISCentralCertProvider` cmdlet 用于禁用 IIS 的中央证书存储功能。中央证书存储允许您将所有 IIS 证书集中存储在一个位置（例如文件共享文件夹）中，然后 IIS 服务器可以从该集中位置获取证书。这样一来，您只需在其中一个位置安装证书即可，无需在每台 IIS 服务器上都单独安装相同的证书。如果您禁用了中央证书存储功能，则需要在所有服务器上分别安装证书。

如果证书存储已被禁用，您可以通过运行 **Enable-IISCentralCertProvider** cmdlet 在任何时候重新启用它。

## 示例

### 示例 1
```
PS C:\> Disable-IISCentralCertProvider
```

此命令会禁用中央证书存储。请注意，在调用 **Disable-IISCentralCertProvider** 时不需要任何参数。另外，系统也不会询问您是否确认要禁用该中央证书存储；只需运行此命令，存储就会被自动禁用。

## 参数

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### System.Object

## 备注

## 相关链接

[Clear-IISCentralCertProvider](./Clear-IISCentralCertProvider.md)

[Enable-IISCentralCertProvider](./Enable-IISCentralCertProvider.md)

[Get-IISCentralCertProvider](./Get-IISCentralCertProvider.md)

[Set-IISCentralCertProvider](./Set-IISCentralCertProvider.md)

[Set-IISCentralCertProviderCredential](./Set-IISCentralCertProviderCredential.md)

