---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
ms.custom: no-azure-ad-ps-ref
online version: https://learn.microsoft.com/powershell/module/adfs/new-adfsazuremfatenantcertificate?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-AdfsAzureMfaTenantCertificate
---

# 新的 AdfsAzureMfaTenantCertificate

## 摘要
为 AD FS 架构创建一个用于连接 Azure MFA 的证书，或者返回当前配置的证书。

## 语法

```
New-AdfsAzureMfaTenantCertificate -TenantId <String> [-Renew <Boolean>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-AdfsAzureMfaTenantCertificate` cmdlet 用于为 Active Directory Federation Services (AD FS) 群集创建证书，以便该集群能够连接到 Azure 多因素身份验证 (MFA)；或者返回当前已配置的证书。

该cmdlet会在本地机器“我的商店”中查找证书，要求其发行者（Issuer）和主题（Subject）满足以下条件：

- `CN = <tenant ID>`
- `OU = Microsoft AD FS Azure MFA`

如果找不到相应的内容，它就会生成新的内容。

## 示例

### 示例 1：创建证书并在 AD FS 架构上启用 Azure 多因素身份验证（MFA）
```
PS C:\> $certbase64 = New-AdfsAzureMfaTenantCertificate -TenantID <your tenant ID>
PS C:\> Add-MgServicePrincipalKey -ServicePrincipalId <service principal ID> -KeyCredential $certbase64
PS C:\> Set-AdfsAzureMfaTenant -TenantId <your tenant ID> -ClientId 981f26a1-7f43-403b-a875-f8b09b8cd720
```

这些命令会为 Azure MFA 创建一个证书，将该证书注册到某个租户账户中，并在 AD FS 系统上启用 Azure MFA 功能。

### 示例 2：确定 Azure MFA 使用的是哪种证书
```
$CertInBase64 = New-AdfsAzureMfaTenantCertificate -TenantID
$cert = Security.Cryptography.X509Certificates.X509Certificate2
$cert | Format-List *
```

在为 Azure MFA 配置了 AD FS 之后，此命令可以确定 Azure MFA 使用的是哪张证书以及该证书的过期时间。

## 参数

### -Renew
更新证书。如果证书已经过期，请不要使用该功能。在这种情况下，现有的过期证书将被替换为一张新证书。

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

### -TenantId
指定 Microsoft Entra 租户 ID 的 GUID 表示形式。您可以在 Microsoft Entra 管理中心的地址栏中找到该 ID，例如：`https://manage.windowsazure.com/contoso.onmicrosoft.com#Workspaces/ActiveDirectoryExtension/Directory/<tenantID_GUID>/directoryQuickStart`

或者，您可以使用 **Login-AzureRmAccount** cmdlet 来获取租户 ID。

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

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
展示了如果该cmdlet被运行会发生的情景。但实际上，该cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-AdfsAzureMfaTenant](./Set-AdfsAzureMfaTenant.md)
