---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
ms.custom: no-azure-ad-ps-ref
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsazuremfatenant?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsAzureMfaTenant
---

# Set-AdfsAzureMfaTenant

## 摘要
使 AD FS 架构能够使用多因素身份验证（MFA）。

## 语法

```
Set-AdfsAzureMfaTenant -TenantId <String> -ClientId <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsAzureMfaTenant` cmdlet 允许 Active Directory Federation Services (AD FS) 集群在证书创建并注册到 Microsoft Entra 租户后使用 Azure 多因素认证 (MFA)。

## 示例

### 示例 1：启用 Azure 多因素身份验证（MFA）
```
PS C:\> $certbase64 = New-AdfsAzureMfaTenantCertificate -TenantID <your tenant ID>
PS C:\> Add-MgServicePrincipalKey -ServicePrincipalId <service principal ID> -KeyCredential $certbase64
PS C:\> Set-AdfsAzureMfaTenant -TenantId <your tenant ID> -ClientId 981f26a1-7f43-403b-a875-f8b09b8cd720
```

此命令为 Azure MFA 创建证书，将其注册到租户账户中，并在 AD FS 系统上启用 Azure MFA 功能。

### 示例 2：确定 Azure 多因素认证（MFA）使用的是哪张证书
```
$CertInBase64 = New-AdfsAzureMfaTenantCertificate -TenantID <your tenant ID>
[Security.Cryptography.X509Certificates.X509Certificate2]([System.Convert]::FromBase64String($CertInBase64))
```

在为 Azure MFA 配置了 AD FS 之后，此命令可以确定 Azure MFA 使用的是哪份证书以及该证书的过期时间。

## 参数

### -ClientId
在 Microsoft Entra ID 中指定该 Azure MFA 应用程序的知名 ID。

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

### -TenantId
指定 Microsoft Entra 租户 ID 的 GUID 表示形式。您可以在 Microsoft Entra 管理中心的地址栏中找到该 GUID，如下例所示：

`https://manage.windowsazure.com/contoso.onmicrosoft.com#Workspaces/ActiveDirectoryExtension/Directory/\<tenantID_GUID\>/directoryQuickStart`

您还可以使用属于 Azure PowerShell 模块的 `Login-AzureRmAccount` cmdlet 来获取租户 ID。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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

## 备注

## 相关链接

[New-AdfsAzureMfaTenantCertificate](./New-AdfsAzureMfaTenantCertificate.md)
