---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmscertinfo?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsCertInfo
---

# 获取 RMS 证书信息

## 摘要
生成一份关于在用户请求中用于AD RMS集群的证书的报告。

## 语法

```
Get-RmsCertInfo -CertificateId <String> [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsCertInfo` cmdlet 会生成一份关于在 Active Directory 权限管理服务（AD RMS）集群中用于用户请求的证书的报告。

要获取报告，请指定您希望获取报告的证书的 CertificateID，然后将 *Path* 参数设置为 AD RMS 提供程序驱动器路径 `<PSDrive>:\`Report，其中 `<PSDrive>` 是提供程序驱动器的 ID。您也可以指定相对路径。例如，点（.）表示当前位置。

使用 `Get-RmsCertChain` cmdlet 来获取您想要生成报告的证书的 *CertificateID*。返回的 *CertificateID* 值仅适用于由 `Get-RmsCertChain` 的 *Path* 参数所指定的集群。您不能使用同一个 *CertificateID* 来标识不同集群中的同一证书。

## 示例

### 示例 1：获取证书报告
```
PS C:\> Get-RmsCertInfo -Path "." -CertificateId "sH+lchPGEP9IKIajmnw5QGUqOl4="
```

该命令会显示特定证书的详细信息。

### 示例 2：传递证书并获取相应的报告
```
PS C:\> $certs= Get-RmsCertChain -Path "." -RequestId 2 | Where {$_.CertificateType -eq 'DRM-CA-Certificate'}
PS C:\> $certs[0] | Get-RmsCertInfo -Path "."
```

该命令将 **Get-RmsCertChain** cmdlet 的过滤结果存储到一个变量中，然后将数组中的第一个证书传递给 **Get-RmsCertInfo** cmdlet，以显示有关该证书的详细信息。

## 参数

### -CertificateId
指定一个唯一的内部证书ID。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

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

### -Path
指定一个提供程序驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，且没有默认值。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsCertChain](./Get-RmsCertChain.md)

[Get-RmsChildCert](./Get-RmsChildCert.md)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

