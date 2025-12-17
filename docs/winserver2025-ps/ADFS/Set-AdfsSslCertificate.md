---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfssslcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsSslCertificate
---

# 设置 AdFS SSL 证书

## 摘要
为 AD FS 的 HTTPS 绑定设置 SSL 证书。

## 语法

```powershell
Set-AdfsSslCertificate -Thumbprint <String> [-Force <Boolean>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-AdfsSslCertificate` cmdlet 用于为 Active Directory Federation Services (AD FS) 的 HTTPS 绑定设置 SSL 证书。使用此 cmdlet 可以更改与 AD FS 服务关联的 SSL 证书。在 Server 2016 上，这是一个多节点 cmdlet，即只需在主节点上运行该命令，所有集群节点都会自动更新；而在 Server 2012R2 上，则需要在 AD FS 集群中的每台服务器上都分别运行此命令。

使用此 cmdlet 将部署方式从当前的方式（即用户证书认证和设备证书认证都使用端口 443）更改为新的方式：在这种新方式中，只有用户证书认证使用非标准端口。请为 `certauth.<联盟服务名称>`（例如 `certauth.contoso.com`）指定一个新的证书，该证书不能包含主题备用名称（Subject Alternative Name, SAN）。

## 示例

### 示例 1：设置证书
```powershell
PS C:\> Set-AdfsSslCertificate -Thumbprint "FC85DDB0FC58E63D8CB52654F22E4BE7900FE349"
```

此命令为 AD FS 的 HTTPS 绑定设置指定的证书。

## 参数

### -Force
```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Thumbprint
用于指定证书的“指纹”（即该证书的唯一标识符）。您指定的指纹对应于安装在联邦服务器本地存储中的证书。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否继续执行该操作。

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

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Get-AdfsSslCertificate](./Get-AdfsSslCertificate.md)

