---
external help file: HgsClient-help.xml
Module Name: HgsClient
online version: https://learn.microsoft.com/powershell/module/hgsclient/test-hgsclientconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Test-HgsClientConfiguration
---

# 测试 HgsClientConfiguration

## 摘要
强制 HGS 客户端与配置好的认证服务器进行交互（即让客户端对这些认证服务器进行验证或确认）。

## 语法

### 主要的；首要的
```
Test-HgsClientConfiguration [-UsePrimary]
```

### 备用方案（Fallback）
```
Test-HgsClientConfiguration [-UseFallback]
```

## 描述
`Test-HgsClientConfiguration` cmdlet 强制 HGS 客户端向 HGS 服务器进行身份验证，并将验证尝试的结果报告回来。任何来自最近身份验证尝试的缓存身份验证健康证书都会被忽略。

## 示例

### 示例 1
```
PS C:\> Test-HgsClientConfiguration
```

使用主HGS服务器尝试进行身份验证（attestation）。如果无法连接到主HGS服务器，并且配置了备用URL，则会使用备用的HGS服务器。

### 示例 2
```
PS C:\> Test-HgsClientConfiguration -UsePrimary
```

尝试使用主HGS服务器进行身份验证（attestation）操作。如果无法连接到主HGS服务器，该命令将失败。

### 示例 3
```
PS C:\> Test-HgsClientConfiguration -UseFallback
```

使用备用的HGS服务器尝试进行身份验证（attestation）操作。

## 参数

### -UseFallback
指定 HGS 客户端应仅针对备用认证服务器进行身份验证（attestation）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: Fallback
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UsePrimary
指定 HGS 客户端应仅对主认证服务器进行认证（即仅接受来自主认证服务器的认证结果）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: Primary
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

## 输入

### 无


## 输出

### Microsoft.ManagementInfrastructure.CimInstance
一个对象，其中包含所使用的认证服务器URL以及认证尝试的结果。

## 备注

## 相关链接

