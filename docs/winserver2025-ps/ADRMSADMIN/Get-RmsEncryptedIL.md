---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.RightsManagementServices.Admin.dll-Help.xml
Module Name: ADRMSADMIN
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adrmsadmin/get-rmsencryptedil?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-RmsEncryptedIL
---

# Get-RmsEncryptedIL

## 摘要
从用于用户请求的发行许可证中获取使用许可信息，该许可证是针对Active Directory Rights Management Services (AD RMS)集群使用的。

## 语法

```
Get-RmsEncryptedIL -ILCertificateId <String> [-Path] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Get-RmsEncryptedIL` cmdlet 会生成一份报告，其中包含有关在 Active Directory Rights Management Services (AD RMS) 集群中用户请求所使用的发行许可证的信息。要使用此 cmdlet，您必须以企业管理员的身份登录。

要获取许可证，请指定您想要获取使用许可信息的证书的 ILCertificateID，然后将 *Path* 参数设置为 AD RMS 提供程序的驱动器路径 `<PSDrive>:\`Report，其中 `<PSDrive>` 是提供程序的驱动器 ID。您也可以指定相对路径。例如，点（.）表示当前位置。

使用 `Get-RmsCertChain` cmdlet 来获取您想要获取使用许可信息的证书的 *ILCertificateID*。返回的 *ILCertificateID* 值仅适用于由 `Get-RmsCertChain` 的 *Path* 参数所标识的集群。您不能使用同一个 *ILCertificateID* 来识别不同集群中的同一张证书。

## 示例

### 示例 1：获取使用许可信息
```
PS C:\> Get-RmsEncryptedIL -Path "." -ILCertificateId "YJ3HGsG/ADg3rLm5LwWGgpAJmz4=" | Out-File -FilePath "C:\temp\RightsPolicyData.xml"
```

此命令从发行许可证中获取使用许可信息，并将结果保存到一个文件中。

## 参数

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

### -ILCertificateId
指定发行许可证证书的哈希ID。

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

### -Path
指定提供者驱动器及其路径，或者当前驱动器上的相对路径。可以使用点（.）来表示当前位置。此参数不支持通配符，且没有默认值。

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
展示了如果该cmdlet被运行会发生什么情况。不过实际上这个cmdlet并没有被运行。

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

[使用 Windows PowerShell 与 AD RMS](https://go.microsoft.com/fwlink/?LinkId=136806)

[Get-RmsCertChain](./Get-RmsCertChain.md)

[Get-RmsCertInfo](./Get-RmsCertInfo.md)

[Get-RmsChildCert](./Get-RmsChildCert.md)

[Get-RmsRequestInfo](./Get-RmsRequestInfo.md)

[Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)

