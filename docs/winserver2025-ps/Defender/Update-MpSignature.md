---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_MpSignature.cdxml-help.xml
Module Name: Defender
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/defender/update-mpsignature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-MpSignature
---

# Update-MpSignature

## 摘要
更新计算机上的反恶意软件定义文件。

## 语法

```
Update-MpSignature [-UpdateSource <UpdateSource>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>]
 [-AsJob] [<CommonParameters>]
```

## 描述
`Update-MpSignature` cmdlet 会使用更新服务器上提供的最新定义来更新反恶意软件库中的定义。

## 示例

#### 示例 1：更新签名
```
PS C:\> Update-MpSignature
```

此命令用于更新反恶意软件定义。默认情况下，该cmdlet会使用通过[SignatureFallbackOrder](Set-MpPreference.yml#-signatureFallbackorder)配置的来源进行更新。如果未配置任何签名回退顺序，则cmdlet会使用默认的更新来源。

### 示例 2：从特定来源更新签名
```
PS C:\> Update-MpSignature -UpdateSource MicrosoftUpdateServer
```

此命令会从微软更新服务器（Microsoft Update Server）获取最新的反恶意软件定义文件并进行更新。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个代表该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，也可以输入会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的cmdlet的最大操作数量。如果省略此参数或输入值为`0`，那么Windows PowerShell®将根据计算机上正在运行的CIM cmdlet的数量来计算该cmdlet的最优限制值。这个限制仅适用于当前执行的cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UpdateSource
指定一个更新源。此 cmdlet 会从您指定的服务器下载更新的定义文件。如果您未指定该参数，cmdlet 将使用通过 [SignatureFallbackOrder](Set-MpPreference.yml#-signaturefallbackorder) 配置的更新源。如果没有配置签名回退顺序，cmdlet 将首先使用 Microsoft Update Server，然后使用 Microsoft Malware Protection Center (MMPC) 作为更新源。该参数的可接受值为：

- InternalDefinitionUpdateServer
- MicrosoftUpdateServer
- MMPC
- FileShares

If you specify the InternalDefinitionUpdateServer setting, the service checks for updates on the Windows Software Update Services (WSUS) server.

```yaml
Type: UpdateSource
Parameter Sets: (All)
Aliases:
Accepted values: InternalDefinitionUpdateServer, MicrosoftUpdateServer, MMPC, FileShares

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接


