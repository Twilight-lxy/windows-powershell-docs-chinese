---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/update-rmsmfgenrollment?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-RmsMfgEnrollment
---

# 更新 RMS 制造商注册信息

## 摘要
更新已注册到 Microsoft Federation Gateway 服务的 AD RMS 服务器的注册信息。

## 语法

```
Update-RmsMfgEnrollment [-TokenCert] [-SigningCert] [-SetCertificatePermissions] [-Force]
 [-GetDefaultCertificate] [-CertificateThumbprint <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Update-RmsMfgEnrollment` cmdlet 用于更新已注册到 Microsoft Federation Gateway 服务的 Active Directory 权限管理服务（AD RMS）服务器的注册信息。

## 示例

### 示例 1：使用默认证书更新支持服务的注册信息
```
PS C:\> Update-RmsMfgEnrollment -GetDefaultCertificate
```

此命令通过检索并使用 AD RMS 默认证书的指纹哈希值来更新当前 AD RMS 服务器对 Microsoft Federation Gateway 支持的注册信息。

### 示例 2：使用指定的证书更新支持服务注册信息
```
PS C:\> Update-RmsMfgEnrollment -CertificateThumbprint "a909502dd82ae41433e6f83886b00d4277a32a7b"
```

此命令使用非默认证书的指纹哈希值来更新当前AD RMS服务器对Microsoft Federation Gateway支持的注册信息。

### 示例 3：更新注册所需的签名证书
```
PS C:\> Update-RmsMfgEnrollment -SigningCert
```

此命令用于更新当前AD RMS服务器对Microsoft Federation Gateway支持的注册状态。

### 示例 4：更新令牌解密证书
```
PS C:\> Update-RmsMfgEnrollment -TokenCert
```

此命令用于更新当前AD RMS服务器的令牌解密证书。

### 示例 5：为 Microsoft Federation Gateway 设置证书权限
```
PS C:\> Update-RmsMfgEnrollment -SetCertificatePermissions
```

此命令用于设置当前 AD RMS 的 Microsoft Federation Gateway 支持注册功能的证书权限。

## 参数

### -CertificateThumbprint
指定一个字符串，其中包含用于通过 Microsoft Federation Gateway 更新注册信息的证书的指纹哈希值。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
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

### -Force
强制命令运行，而无需请求用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -GetDefaultCertificate
当指明这一点时，表示应获取 AD RMS 默认证书的指纹哈希值，并使用该哈希值来更新与 Microsoft Federation Gateway 的注册信息。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -SetCertificatePermissions
当指定此选项时，表示需要在通过 Microsoft Federation Gateway 进行的 AD RMS 服务器注册过程中设置相应的权限。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -SigningCert
当指定此选项时，表示需要更新（或在元数据中刷新）Microsoft Federation Gateway的签名证书，以便用于当前的AD RMS服务器注册过程。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TokenCert
当指定该选项时，表示需要更新令牌解密证书，以便在与 Microsoft Federation Gateway 进行 AD RMS 服务器注册时使用该证书。

您可以根据需要更新令牌解密证书或 Microsoft Federation Gateway 证书。由于令牌解密证书是 AD RMS 集群的 SSL 证书，因此如果集群的 SSL 证书过期，就必须更新该令牌解密证书。更新令牌解密证书后，还需要为 AD RMS Services 组授予在 AD RMS 集群中的所有服务器上访问该证书的权限。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

